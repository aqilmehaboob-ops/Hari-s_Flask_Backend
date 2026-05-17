# Buildivine Store - Backend API

A complete e-commerce backend built for a real client - Buildivine Jewellery Store. Built with Flask and deployed on Render.

**Live API:** https://buildivine-store-api.onrender.com

## Tech Stack
Python • Flask • SQLAlchemy • JWT • SQLite • REST API

## Features
- JWT Authentication (Register & Login)
- Role-Based Access Control (Admin only can add products)
- Jewellery inventory management with stock tracking
- Cart system with add/remove items
- Order placement with automatic inventory deduction
- Duplicate product handling with quantity updates

## API Routes

### Auth
| Method | Route | Description |
|--------|-------|-------------|
| POST | /register | Register new user |
| POST | /login | Login and receive JWT token |

### Jewellery
| Method | Route | Description |
|--------|-------|-------------|
| GET | /jwellerys | Get all products |
| POST | /jwellerys | Add new product (Admin only) |
| GET | /jwellerys/filter?type=ring | Filter by type |

### Cart
| Method | Route | Description |
|--------|-------|-------------|
| POST | /cart | Add item to cart |
| DELETE | /cart/<jwellery_id> | Remove item from cart |
| GET | /cart | View cart items |

### Orders
| Method | Route | Description |
|--------|-------|-------------|
| POST | /orders | Place an order |
| GET | /orders | View my orders |

## Setup

```bash
git clone https://github.com/aqilmehaboob-ops/Hari-s_Flask_Backend
cd Hari-s_Flask_Backend
pip install -r requirements.txt
python run.py
```

## Testing
Use Postman to test the API.
1. Register a user at /register
2. Login at /login to get JWT token
3. Add token to Authorization header as Bearer token
4. Test protected routes

## Business Logic
- Stock automatically reduces on every order
- Orders rejected if item is out of stock
- Admin access required to add new jewellery items
- Duplicate products update existing inventory instead of creating new entry

## Developer
Built by Aqil Mulangery
github.com/aqilmehaboob-ops
