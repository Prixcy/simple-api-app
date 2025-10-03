# Todo List App - Three-Tier Architecture

A modern todo list application built with a three-tier architecture using **Streamlit** (frontend), **FastAPI** (backend), and **SQLite** (database), all containerized with Docker Compose.

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │    │   Database      │
│   (Streamlit)   │◄──►│   (FastAPI)     │◄──►│   (SQLite)      │
│   Port: 8501    │    │   Port: 8000    │    │   File: todos.db│
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## ✨ Features

- **User Management**: Sign up, sign in, and user authentication
- **Todo CRUD Operations**: Create, read, update, and delete todos
- **Rich Todo Management**: 
  - Add descriptions and reminder times
  - Mark todos as completed/incomplete
  - Edit existing todos inline
  - Delete todos with confirmation
- **Smart Filtering & Sorting**:
  - Filter by completion status
  - Sort by creation date, title, or status
- **Statistics Dashboard**: Track completion rates and progress
- **Responsive UI**: Modern, clean interface with custom styling
- **Dockerized**: Easy deployment with Docker Compose

## 🚀 Quick Start

### Prerequisites

- Docker and Docker Compose installed
- Git (for cloning the repository)

### Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd simple_api_app
   ```

2. **Start the application**:
   ```bash
   docker compose up --build
   ```

3. **Access the application**:
   - **Frontend (Streamlit)**: http://localhost:8501
   - **Backend API**: http://localhost:8000
   - **API Documentation**: http://localhost:8000/docs

### First Time Setup

1. Open http://localhost:8501 in your browser
2. Click "Sign Up" in the sidebar
3. Create your account with username and email
4. Start adding your todos!

## 🛠️ Development

### Running Locally (without Docker)

1. **Install dependencies**:
   ```bash
   pip install poetry
   poetry install
   ```

2. **Initialize the database**:
   ```bash
   python init_db.py
   ```

3. **Start the backend**:
   ```bash
   python -m uvicorn app.backend:app --reload --host 0.0.0.0 --port 8000
   ```

4. **Start the frontend** (in a new terminal):
   ```bash
   streamlit run app/frontend.py --server.port 8501
   ```

### Database Management

- **Initialize database**: `python init_db.py`
- **Reset database**: `python init_db.py --reset`
- **Database location**: `./data/todos.db` (when using Docker)

## 📚 API Documentation

The FastAPI backend provides a RESTful API with the following endpoints:

### Users
- `POST /users/` - Create a new user
- `GET /users/{user_id}` - Get user by ID

### Todos
- `POST /todos/` - Create a new todo
- `GET /todos/` - Get all todos for a user
- `GET /todos/{todo_id}` - Get a specific todo
- `PUT /todos/{todo_id}` - Update a todo
- `DELETE /todos/{todo_id}` - Delete a todo

Visit http://localhost:8000/docs for interactive API documentation.

## 🐳 Docker Services

The application now runs a single backend service (FastAPI) and uses a SQLite file persisted on the host via bind mount at `./database/todos.db`.

### Docker Commands

```bash
# Start all services
docker-compose up

# Start in background
docker-compose up -d

# Rebuild and start
docker-compose up --build

# Stop all services
docker-compose down

# View logs
docker-compose logs -f

# View logs for specific service
docker-compose logs -f backend
```

## 📁 Project Structure

```
simple_api_app/
├── app/
│   ├── __init__.py
│   ├── backend.py          # FastAPI backend
│   └── frontend.py         # Streamlit frontend
├── data/                   # SQLite database (created by Docker)
├── docker-compose.yml      # Docker Compose configuration
├── Dockerfile.backend      # Backend Dockerfile
├── Dockerfile.frontend     # Frontend Dockerfile
├── init_db.py             # Database initialization script
├── pyproject.toml         # Python dependencies
└── README.md              # This file
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
DATABASE_URL=sqlite:///./data/todos.db
API_HOST=0.0.0.0
API_PORT=8000
FRONTEND_PORT=8501
API_BASE_URL=http://backend:8000
DEBUG=True
```

### Customization

- **Database**: Modify `DATABASE_URL` in `docker-compose.yml`
- **Ports**: Change port mappings in `docker-compose.yml`
- **API URL**: Update `API_BASE_URL` in `app/frontend.py`

## 🧪 Testing

### Manual Testing

1. **API Testing**: Use the interactive docs at http://localhost:8000/docs
2. **Frontend Testing**: Test all features through the Streamlit interface
3. **Database Testing**: Verify data persistence across restarts

### Sample Data

The database initialization script creates sample data for testing:
- Demo user account
- Sample todos with different completion states

## 🚀 Deployment

### Production Considerations

1. **Security**: Update CORS settings in `backend.py`
2. **Database**: Consider using PostgreSQL for production
3. **Environment**: Use proper environment variables
4. **Monitoring**: Add logging and monitoring
5. **SSL**: Configure HTTPS for production

### Docker Production

```bash
# Build production images
docker-compose -f docker-compose.prod.yml up --build

# Use Docker Swarm or Kubernetes for orchestration
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Troubleshooting

### Common Issues

1. **Port conflicts**: Change ports in `docker-compose.yml`
2. **Database errors**: Run `python init_db.py --reset`
3. **Connection issues**: Check if all services are running
4. **Permission errors**: Ensure Docker has proper permissions

### Getting Help

- Check the logs: `docker-compose logs`
- Verify service status: `docker-compose ps`
- Test API endpoints: Visit http://localhost:8000/docs

---

**Happy Todo-ing! 🎉**

