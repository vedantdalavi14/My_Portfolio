from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure CORS for Vercel deployment
CORS(app, resources={
    r"/api/contact": {
        "origins": [
            "http://localhost:5000",  # Local development
            "http://localhost:3000",   # Local development alternative port
            "https://*.vercel.app",    # Vercel deployment URLs
            "https://your-portfolio-domain.com"  # Your custom domain if any
        ],
        "methods": ["POST"],
        "allow_headers": ["Content-Type"]
    }
})

# Email configuration
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS', 'vedantdalavi14@gmail.com')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
OWNER_EMAIL = os.getenv('OWNER_EMAIL', 'vedantdalavi14@gmail.com')

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def send_email_notification(name, email, subject, message):
    """Send email notification to site owner"""
    try:
        # Create message
        msg = MIMEMultipart('alternative')
        msg['Subject'] = f'New Contact Form Submission: {subject}'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = OWNER_EMAIL
        msg['Reply-To'] = email

        # Create HTML content
        html = f"""
        <html>
            <body>
                <h2>New Contact Form Submission</h2>
                <p><strong>From:</strong> {name} &lt;{email}&gt;</p>
                <p><strong>Subject:</strong> {subject}</p>
                <p><strong>Message:</strong></p>
                <div style="background-color: #f8f9fa; padding: 15px; border-radius: 5px;">
                    {message.replace('\n', '<br>')}
                </div>
            </body>
        </html>
        """

        # Create plain text version
        text = f"""
        New Contact Form Submission

        From: {name} ({email})
        Subject: {subject}

        Message:
        {message}
        """

        # Attach both versions
        msg.attach(MIMEText(text, 'plain'))
        msg.attach(MIMEText(html, 'html'))

        # Send email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        
        logger.info(f"Email notification sent successfully to {OWNER_EMAIL}")
        return True
    except Exception as e:
        logger.error(f"Failed to send email notification: {str(e)}")
        return False

@app.route('/api/contact', methods=['POST'])
def contact():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        name = data.get('name')
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')
        
        if not all([name, email, message]):
            return jsonify({"error": "Missing required fields"}), 400
        
        # Validate email format
        if '@' not in email or '.' not in email:
            return jsonify({"error": "Invalid email format"}), 400
        
        # Send email notification
        email_sent = send_email_notification(name, email, subject, message)
        
        response = {
            "success": True,
            "message": "Your message has been received! I'll get back to you soon.",
            "email_sent": email_sent
        }
        
        if not email_sent:
            response["warning"] = "Message received but email notification failed to send"
        
        return jsonify(response), 200
    except Exception as e:
        logger.error(f"Error processing contact form: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500

# Vercel serverless function handler
def handler(request):
    if request.path == '/api/contact':
        return contact()
    return {"statusCode": 404, "body": "Not Found"}

if __name__ == '__main__':
    # Check for required environment variables
    if not EMAIL_PASSWORD:
        logger.warning("Email password not found in environment variables. Email notifications will not work.")
    
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=os.environ.get("FLASK_DEBUG", "False").lower() == "true")