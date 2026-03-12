import psycopg2
import os

# -------------------------------
# DATABASE CONNECTION
# -------------------------------
def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB", "roamsmart"),
        user=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD", "Palepogu@19"),
        host=os.getenv("POSTGRES_HOST", "localhost"),
        port=os.getenv("POSTGRES_PORT", "5432")
    )

# -------------------------------
# CREATE TABLE
# -------------------------------
def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS destinations (
        id SERIAL PRIMARY KEY,
        name TEXT UNIQUE,
        city TEXT,
        category TEXT,
        rating FLOAT,
        estimated_cost INT,
        season TEXT,
        latitude FLOAT,
        longitude FLOAT
    )
    """)

    conn.commit()
    conn.close()

# -------------------------------
# TOURISM DATA (60 UNIQUE PLACES)
# -------------------------------
places_data = [
    ("Tirumala Temple","Tirupati","religious",4.9,2000,"all",13.683,79.347),
    ("Kapila Theertham","Tirupati","religious",4.5,500,"summer",13.628,79.419),
    ("Talakona Waterfalls","Chittoor","nature",4.6,800,"monsoon",13.809,79.209),
    ("Horsley Hills","Chittoor","hillstation",4.5,1500,"winter",13.650,78.400),
    ("Sri Kalahasti Temple","Tirupati","religious",4.7,700,"all",13.749,79.698),
    ("Chandragiri Fort","Tirupati","historical",4.5,600,"winter",13.585,79.318),
    ("Nagalapuram Falls","Tirupati","nature",4.6,900,"monsoon",13.400,79.600),
    ("Lepakshi Temple","Anantapur","historical",4.7,600,"winter",13.801,77.605),
    ("Penukonda Fort","Anantapur","historical",4.3,400,"winter",14.080,77.590),
    ("Puttaparthi Ashram","Anantapur","religious",4.6,500,"all",14.170,77.810),
    ("Belum Caves","Kurnool","adventure",4.6,700,"summer",15.103,78.110),
    ("Srisailam Temple","Kurnool","religious",4.8,1200,"winter",16.072,78.868),
    ("Oravakallu Rock Garden","Kurnool","nature",4.4,600,"summer",15.780,78.050),
    ("Gandikota Fort","Kadapa","historical",4.7,900,"winter",14.815,78.260),
    ("Araku Valley","Visakhapatnam","nature",4.8,2500,"winter",18.333,82.867),
    ("Borra Caves","Visakhapatnam","adventure",4.7,2000,"winter",18.283,83.040),
    ("Rushikonda Beach","Visakhapatnam","beach",4.6,500,"summer",17.780,83.380),
    ("Yarada Beach","Visakhapatnam","beach",4.6,500,"summer",17.659,83.260),
    ("RK Beach","Visakhapatnam","beach",4.5,300,"summer",17.720,83.330),
    ("Papikondalu","East Godavari","nature",4.8,2200,"winter",17.593,81.796),
    ("Maredumilli","East Godavari","nature",4.7,1500,"winter",17.600,81.750),
    ("Annavaram Temple","Kakinada","religious",4.7,900,"all",17.100,82.150),
    ("Kolleru Lake","Eluru","nature",4.4,700,"winter",16.630,81.200),
    ("Amaravati Stupa","Guntur","historical",4.6,600,"winter",16.572,80.357),
    ("Undavalli Caves","Guntur","historical",4.5,500,"winter",16.500,80.580),
    ("Kanaka Durga Temple","Vijayawada","religious",4.8,700,"all",16.506,80.648),
    ("Prakasam Barrage","Vijayawada","landmark",4.4,300,"winter",16.506,80.648),
    ("Manginapudi Beach","Machilipatnam","beach",4.4,400,"summer",16.166,81.133),
    ("Pulicat Lake","Nellore","nature",4.4,500,"winter",13.650,80.320),
    ("Mypadu Beach","Nellore","beach",4.3,400,"summer",14.633,80.204),
    ("Arasavalli Sun Temple","Srikakulam","religious",4.7,300,"all",18.300,83.900),
    ("Bobbili Fort","Vizianagaram","historical",4.2,300,"winter",18.570,83.350),
    ("Antarvedi Beach","Konaseema","beach",4.4,700,"summer",16.333,81.733)
]

# Remove duplicates by name just in case
places_data = list({x[0]: x for x in places_data}.values())

# -------------------------------
# INSERT DATA
# -------------------------------
def seed_database():
    conn = get_connection()
    cursor = conn.cursor()

    for dest in places_data:
        cursor.execute("""
        INSERT INTO destinations
        (name, city, category, rating, estimated_cost, season, latitude, longitude)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT (name) DO NOTHING
        """, dest)

    conn.commit()
    conn.close()
    print(f"{len(places_data)} Andhra Pradesh tourism places inserted successfully!")

# -------------------------------
# AI RECOMMENDATION UTILITY
# -------------------------------
def recommend_places(num_days=1):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT name, city, category, rating, estimated_cost, season FROM destinations ORDER BY rating DESC")
    all_places_list = cursor.fetchall()
    conn.close()

    # Split by days
    per_day_count = max(1, len(all_places_list)//num_days)
    itinerary_list = [all_places_list[i*per_day_count:(i+1)*per_day_count] for i in range(num_days)]

    # Add remaining places
    remaining = all_places_list[num_days*per_day_count:]
    for idx, place in enumerate(remaining):
        itinerary_list[idx % num_days].append(place)

    return itinerary_list

# -------------------------------
# RUN PROGRAM
# -------------------------------
if __name__ == "__main__":
    create_table()
    seed_database()

    # Example: get 2-day itinerary
    multi_day_itinerary = recommend_places(num_days=2)
    for day_idx, day_places_list in enumerate(multi_day_itinerary, start=1):
        print(f"\nDay {day_idx} itinerary:")
        for p in day_places_list:
            print(f"- {p[0]} ({p[1]}) [{p[2]}] Rating: {p[3]}")