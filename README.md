# Vedya's Portfolio Website

A modern, responsive portfolio website built with HTML, Tailwind CSS, and a Flask backend, deployed on Vercel.

## Features

- Responsive design for all device sizes
- Modern UI with smooth animations and transitions
- Interactive project showcases
- Skills section with visual icons
- Contact form with email notifications
- Dark mode support

## Technology Stack

- **Frontend**: HTML with Tailwind CSS
- **Backend**: Python with Flask
- **Deployment**: Vercel
- **Email Service**: Gmail SMTP

## Local Development

### Prerequisites

- Python 3.7+
- Git
- GitHub account
- Vercel account

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/portfolio.git
   cd portfolio
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file:
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` with your email credentials.

5. Run the development server:
   ```bash
   python app.py
   ```

6. Visit `http://localhost:5000` in your browser.

## Deployment

### GitHub Setup

1. Create a new repository on GitHub
2. Push your code:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/your-username/portfolio.git
   git push -u origin main
   ```

### Vercel Deployment

1. Go to [Vercel](https://vercel.com)
2. Import your GitHub repository
3. Configure the following settings:
   - Framework Preset: Other
   - Build Command: (leave empty)
   - Output Directory: .
   - Install Command: pip install -r requirements.txt

4. Add Environment Variables:
   - `EMAIL_ADDRESS`
   - `EMAIL_PASSWORD` (Gmail app password)
   - `OWNER_EMAIL`
   - `FLASK_DEBUG=False`

5. Deploy!

## Environment Variables

Create a `.env` file with the following variables:
```
EMAIL_ADDRESS=your-email@gmail.com
EMAIL_PASSWORD=your-app-specific-password
OWNER_EMAIL=your-email@gmail.com
FLASK_DEBUG=False
PORT=5000
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 