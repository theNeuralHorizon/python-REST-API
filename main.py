from fastapi import FastAPI, HTTPException

app = FastAPI()

# In-memory database for demonstration purposes
user_db: dict[str, dict] = {}

@app.get("/user/{user_id}")
async def get_user(user_id: str):
    """
    Retrieve a user profile by ID.
    """
    user = user_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/user")
async def create_user(user: dict):
    """
    Create a new user profile.
    Expect JSON with 'email', 'name', and 'date_of_birth'.
    """
    required_fields = ["email", "name", "date_of_birth"]
    if not all(field in user for field in required_fields):
        raise HTTPException(status_code=400, detail=f"Missing required fields: {required_fields}")
    
    user_id = str(len(user_db) + 1)  # Generate a simple unique ID
    user_db[user_id] = user
    return {"user_id": user_id, "message": "User created successfully"}