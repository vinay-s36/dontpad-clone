# Dontpad clone
Dontpad Clone is a web-based application inspired by the original [Dontpad](https://dontpad.com) platform. It is designed for creating, editing, and sharing text through unique URLs, offering simplicity and real-time updates.

## Prerequisites
- Python 3.x
- PostgreSQL

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/vinay-s36/dontpad-clone.git
cd dontpad-clone
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv

# On Unix/macOS
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
1. For local development: Install and run PostgreSQL on your machine
2. For cloud hosting: Create a database on Neon DB or another PostgreSQL provider and save the database connection string for the next step

### 5. Environment Configuration
1. Create a copy of the example environment file:
   ```bash
   cp .env.example .env
   ```
2. Update `.env` with your database credentials:
   ```plaintext
   DATABASE_URL=postgresql://username:password@host:port/dbname
   ```

### 6. Launch Application
```bash
python app.py
```

## Usage
Once running, access the application at: `http://127.0.0.1:5000`
