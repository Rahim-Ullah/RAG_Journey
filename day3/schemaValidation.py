from pydantic import BaseModel, ConfigDict, ValidationError, Field, AfterValidator, BeforeValidator, field_validator
from typing import Optional

class BasicUser(BaseModel):
    name: str
    email: str
    age: Optional[int] = None
    
class User(BasicUser):
    is_active: bool = True
    
class UserLogin(BaseModel):
    username: str
    password: str = Field(..., min_length=6, max_length=20)
    
    @field_validator("password")
    @classmethod
    def validate_password(cls, password: str) -> str:
        if not any(char.isupper() for char in password):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(char.islower() for char in password):
            raise ValueError("Password must contain at least one lowercase letter")
        if not any(char.isdigit() for char in password):
            raise ValueError("Password must contain at least one digit")
        if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in password):
            raise ValueError("Password must contain at least one special character")
        return password
    
    model_config = ConfigDict(
        from_attributes=True
    )
    
    
# Password Requirements
# Length > 5 and < 20
# At least one uppercase letter
# At least one lowercase letter
# At least one digit
# At least one special character

# Type Annotation
a: int = 10
b: str = "Hello"
c: float = 73.32


def func(a: int , b: int) -> int:
    return a + b

func(1, 2)

def func2(a: str, b: str) -> str:
    pass
user = UserLogin(username="Alice", password="Password123!")
print(user.username)

user2 = {
    "username": "Bob",
    "password": "Password123!"
}

user2Obj = UserLogin(
    username=user2["username"],
    password=user2["password"]
)

user2Obj = UserLogin(**user2)
# print(user2.model_dump_json())

# try:
#     obj = User(name="Alice", email=244)
# except ValidationError as e:
#     print("Error")

# print(obj)


# Decoraotors
# Static methods Vs Class methods
# Gnerators
# Depcrycated
# **Kargs Vs *args

l1 = [True, False, False, False]
print(all(l1))

# Structured Output Prompt
#   - Support Tickets
#   - Input Support Ticket
#   - Subject, Description
#   {
#      "category": "payment-failure" | "checkin-issue" | "Sales Cancellation" | "General Inquiry" | "Technical Support"
#      "priority": "low" | "medium" | "high"
#      "spam": "yes" | "no"
#  }

# The category is Payment Failure, the priority is high, and the spam is no.
# Category: payment-failure, Priority: high, Spam: no

# enums -- Enumerations
#   - Named values

from enum import Enum

class TicketCategory(str, Enum):
    PAYMENT_FAILURE = "payment-failure"
    CHECKIN_ISSUE = "checkin-issue"
    SALES_CANCELLATION = "sales-cancellation"
    GENERAL_INQUIRY = "general-inquiry"
    TECHNICAL_SUPPORT = "technical-support"
    
class TicketPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    
class TicketSpam(str, Enum):
    YES = "yes"
    NO = "no"  

class SupportTicket(BaseModel):
    category: TicketCategory = Field(description="Category of the support ticket")
    priority: TicketPriority = Field(description="Priority level of the support ticket")
    spam: TicketSpam = Field(description="Indicates if the ticket is spam or not")