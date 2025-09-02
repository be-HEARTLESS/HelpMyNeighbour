# Development Setup Guide

This guide will help you set up the Help My Neighbour project for local development.

## Project Structure

```
help-my-neighbour/
├── frontend/                 # React.js frontend application
│   ├── src/
│   │   ├── components/      # Reusable React components
│   │   ├── pages/           # Page-level components
│   │   ├── store/           # Redux state management
│   │   ├── services/        # API service layer
│   │   ├── types/           # TypeScript type definitions
│   │   └── utils/           # Utility functions
│   ├── public/              # Static assets
│   └── package.json         # Frontend dependencies
├── backend/                  # Django REST API backend
│   ├── helpneighbour/       # Django project configuration
│   ├── users/               # User management app
│   ├── help_requests/       # Help requests app
│   ├── requirements.txt     # Python dependencies
│   └── manage.py            # Django management script
├── docs/                     # Project documentation
├── docker-compose.yml        # Docker services configuration
└── README.md                # Main project documentation
```

## Prerequisites

Make sure you have the following installed:

- **Node.js** (v16 or higher)
- **Python** (v3.9 or higher)
- **Git**
- **Docker & Docker Compose** (optional, for containerized development)

## Quick Start (Local Development)

### 1. Clone the Repository

```bash
git clone <repository-url>
cd help-my-neighbour
```

### 2. Setup Backend (Django)

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\\Scripts\\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install django djangorestframework django-cors-headers

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

The backend will be available at `http://localhost:8000`

### 3. Setup Frontend (React)

Open a new terminal window:

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

The frontend will be available at `http://localhost:3000`

## Available API Endpoints

### Health Check
- **GET** `/api/health/` - API health check

### Users
- **GET** `/api/users/me/` - User profile (placeholder)

### Help Requests
- **GET** `/api/help-requests/` - List help requests (placeholder)

## Development Features Implemented

### Frontend (React + TypeScript)
- ✅ **Project Structure**: Well-organized component architecture
- ✅ **Routing**: React Router setup with protected routes
- ✅ **State Management**: Redux Toolkit configuration
- ✅ **Type Safety**: Comprehensive TypeScript types
- ✅ **Styling**: Tailwind CSS framework (partial setup)
- ✅ **Authentication Flow**: Login/register pages structure
- ✅ **Landing Page**: Beautiful home page with features showcase
- ✅ **Layout Components**: Header, Sidebar, and main layout
- ✅ **API Integration**: Axios-based service layer

### Backend (Django + DRF)
- ✅ **Project Setup**: Django with REST Framework
- ✅ **CORS Configuration**: Frontend-backend communication enabled
- ✅ **App Structure**: Modular Django apps (users, help_requests)
- ✅ **API Endpoints**: Basic placeholder endpoints
- ✅ **Database**: SQLite for development (ready for MongoDB)

### Additional Features
- ✅ **Docker Support**: Complete containerization setup
- ✅ **Documentation**: Comprehensive project documentation
- ✅ **Environment Configuration**: Environment variable management

## Next Steps for Full Implementation

### Phase 1: Core Features
1. **User Authentication**
   - JWT token authentication
   - User registration and login
   - Profile management
   - Email verification

2. **Help Request System**
   - CRUD operations for help requests
   - Category and urgency management
   - Image upload support
   - Location-based filtering

3. **Database Models**
   - User profile extension
   - Help request models
   - Response/offer models
   - Rating and review system

### Phase 2: Advanced Features
1. **Real-time Communication**
   - WebSocket integration with Django Channels
   - In-app messaging system
   - Push notifications with Firebase

2. **Location Services**
   - Google Maps integration
   - Geolocation services
   - Proximity-based matching

3. **Community Features**
   - Trusted circles
   - Community posts
   - Event organization

### Phase 3: Production Ready
1. **Security & Performance**
   - Input validation and sanitization
   - Rate limiting
   - Database optimization
   - Caching with Redis

2. **Testing & Quality**
   - Unit tests for backend
   - Component tests for frontend
   - E2E testing with Cypress
   - Code quality tools (ESLint, Prettier, Black)

3. **Deployment**
   - Production Docker configuration
   - CI/CD pipeline
   - Cloud deployment (AWS/GCP)
   - Domain and SSL setup

## Available Scripts

### Frontend
- `npm start` - Start development server
- `npm build` - Build for production
- `npm test` - Run tests
- `npm run eject` - Eject from Create React App

### Backend
- `python manage.py runserver` - Start development server
- `python manage.py migrate` - Apply database migrations
- `python manage.py makemigrations` - Create new migrations
- `python manage.py createsuperuser` - Create admin user
- `python manage.py shell` - Open Django shell

## Environment Variables

### Frontend (.env)
```env
REACT_APP_API_URL=http://localhost:8000/api
REACT_APP_GOOGLE_MAPS_API_KEY=your_google_maps_key
```

### Backend (.env)
```env
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///db.sqlite3
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

## Troubleshooting

### Common Issues

1. **Port Already in Use**
   - Frontend: Change port with `PORT=3001 npm start`
   - Backend: Change port with `python manage.py runserver 8001`

2. **Module Not Found Errors**
   - Frontend: Delete `node_modules` and run `npm install`
   - Backend: Activate virtual environment and reinstall dependencies

3. **CORS Issues**
   - Ensure `django-cors-headers` is installed and configured
   - Check `CORS_ALLOWED_ORIGINS` in Django settings

4. **Database Issues**
   - Delete `db.sqlite3` and run migrations again
   - Check database connectivity and permissions

### Getting Help

- Check the issue tracker in the repository
- Review Django and React documentation
- Join our community discussions

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.
