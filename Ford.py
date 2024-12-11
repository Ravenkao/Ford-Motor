# Ford Motor_Cost-benefit analysis
# Step 1: Define LiDAR models data
lidar_data = [
    {"type": "Mechanical", "price_min": 1000, "price_max": 10000, "durability": "Moderate", "performance": "High",
     "applications": "Large mapping"},
    {"type": "Solid-State", "price_min": 10000, "price_max": 100000, "durability": "High", "performance": "High-speed",
     "applications": "Dynamic environments"},
    {"type": "Hybrid", "price_min": 5000, "price_max": 50000, "durability": "Moderate to High",
     "performance": "Balanced", "applications": "Comprehensive 3D perception"}
]

# Step 2: Define weight for cost-benefit analysis
weights = {"price": 0.4, "durability": 0.3, "performance": 0.3}


# Step 3: Scoring system function
def score_lidar(lidar):
    # Normalize price: Lower price, higher score
    avg_price = (lidar["price_min"] + lidar["price_max"]) / 2
    price_score = 1 / avg_price

    # Durability: Assign numeric values
    durability_score = {"Low": 0.3, "Moderate": 0.6, "Moderate to High": 0.8, "High": 1.0}[lidar["durability"]]

    # Performance: Assign numeric values
    performance_score = {"Low": 0.3, "Moderate": 0.6, "High": 1.0, "High-speed": 1.0, "Balanced": 0.8}[
        lidar["performance"]]

    # Weighted score
    total_score = (
            weights["price"] * price_score +
            weights["durability"] * durability_score +
            weights["performance"] * performance_score
    )
    return total_score


# Step 4: Calculate scores and rank LiDAR options
lidar_scores = [{**lidar, "score": score_lidar(lidar)} for lidar in lidar_data]
lidar_scores = sorted(lidar_scores, key=lambda x: x["score"], reverse=True)

# Step 5: Print results
print("LiDAR Cost-Benefit Analysis Results:")
for lidar in lidar_scores:
    avg_price = (lidar["price_min"] + lidar["price_max"]) / 2
    print(
        f"{lidar['type']} LiDAR - Average Price: ${avg_price:.2f}, Score: {lidar['score']:.4f}, Durability: {lidar['durability']}, Performance: {lidar['performance']}")


