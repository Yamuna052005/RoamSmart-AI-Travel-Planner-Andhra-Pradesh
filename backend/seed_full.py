import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB", "roamsmart"),
        user=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD", "Palepogu@19"),
        host=os.getenv("POSTGRES_HOST", "localhost"),
        port=os.getenv("POSTGRES_PORT", "5432")
    )

places_data = [
    # Tirupati / Chittoor
    ("Tirumala Temple","Tirupati","religious",4.8,2000,"summer",13.6830,79.3500,
     "https://www.alamy.com/stock-photo-the-main-gateway-to-lord-venkateshvara-tem"),
    ("Kapila Theertham","Tirupati","religious",4.5,1500,"summer",13.6288,79.4192,
     "https://upload.wikimedia.org/wikipedia/commons/4/4a/Kapila_Theertham_Temple_Tirupati.jpg"),
    ("Sri Venkateswara Zoo","Tirupati","wildlife",4.2,1000,"winter",13.6270,79.4200,
     "https://upload.wikimedia.org/wikipedia/commons/5/5a/Sri_Venkateswara_Zoological_Park.jpg"),
    ("Talakona Waterfalls","Chittoor","nature",4.6,900,"monsoon",13.8090,79.2090,
     "https://upload.wikimedia.org/wikipedia/commons/6/6d/Talakona_Waterfalls.jpg"),
    ("Horsley Hills","Chittoor","hillstation",4.5,1500,"summer",13.6500,78.4000,
     "https://upload.wikimedia.org/wikipedia/commons/9/9d/Horsley_Hills_View.jpg"),

    # Anantapur
    ("Lepakshi Temple","Anantapur","historical",4.6,600,"winter",13.8015,77.6050,
     "https://upload.wikimedia.org/wikipedia/commons/2/2f/Lepakshi_Temple.jpg"),
    ("Penukonda Fort","Anantapur","historical",4.3,400,"winter",14.0800,77.5900,
     "https://upload.wikimedia.org/wikipedia/commons/8/8a/Penukonda_Fort.jpg"),
    ("Puttaparthi Ashram","Anantapur","religious",4.7,500,"summer",14.1700,77.8100,
     "https://upload.wikimedia.org/wikipedia/commons/7/7f/Puttaparthi_Ashram.jpg"),

    # Kurnool
    ("Belum Caves","Kurnool","adventure",4.5,700,"summer",15.1033,78.1103,
     "https://upload.wikimedia.org/wikipedia/commons/3/3d/Belum_Caves.jpg"),
    ("Srisailam Temple","Kurnool","religious",4.7,800,"winter",16.0725,78.8680,
     "https://upload.wikimedia.org/wikipedia/commons/4/4c/Srisailam_Temple.jpg"),
    ("Oravakallu Rock Garden","Kurnool","nature",4.4,600,"summer",15.7800,78.0500,
     "https://upload.wikimedia.org/wikipedia/commons/5/5f/Oravakallu_Rock_Garden.jpg"),

    # Kadapa
    ("Gandikota Fort","Kadapa","historical",4.7,900,"winter",14.8150,78.2600,
     "https://upload.wikimedia.org/wikipedia/commons/6/6e/Gandikota_Fort.jpg"),
    ("Ameen Peer Dargah","Kadapa","religious",4.5,300,"summer",14.4700,78.8200,
     "https://upload.wikimedia.org/wikipedia/commons/1/1a/Ameen_Peer_Dargah.jpg"),

    # Visakhapatnam
    ("Araku Valley","Visakhapatnam","nature",4.8,3000,"monsoon",18.3330,82.8670,
     "https://upload.wikimedia.org/wikipedia/commons/7/7a/Araku_Valley.jpg"),
    ("Borra Caves","Visakhapatnam","adventure",4.6,2200,"winter",18.2830,83.0400,
     "https://upload.wikimedia.org/wikipedia/commons/8/8b/Borra_Caves.jpg"),
    ("Yarada Beach","Visakhapatnam","beach",4.6,600,"summer",17.6590,83.2600,
     "https://upload.wikimedia.org/wikipedia/commons/9/9c/Yarada_Beach.jpg"),
    ("Rushikonda Beach","Visakhapatnam","beach",4.5,500,"summer",17.7800,83.3800,
     "https://upload.wikimedia.org/wikipedia/commons/2/2a/Rushikonda_Beach.jpg"),
    ("Kailasagiri Hill Park","Visakhapatnam","nature",4.5,400,"winter",17.7466,83.3386,
     "https://upload.wikimedia.org/wikipedia/commons/3/3b/Kailasagiri_Hill_Park.jpg"),
    ("Simhachalam Temple","Visakhapatnam","religious",4.7,500,"summer",17.7660,83.2500,
     "https://upload.wikimedia.org/wikipedia/commons/4/4d/Simhachalam_Temple.jpg"),

    # East Godavari
    ("Papikondalu Hills","East Godavari","nature",4.7,2000,"monsoon",17.5930,81.7960,
     "https://upload.wikimedia.org/wikipedia/commons/5/5e/Papikondalu_Hills.jpg"),
    ("Maredumilli Forest","East Godavari","nature",4.6,1200,"monsoon",17.6000,81.7500,
     "https://upload.wikimedia.org/wikipedia/commons/6/6f/Maredumilli_Forest.jpg"),
    ("Draksharamam Temple","East Godavari","religious",4.6,400,"summer",16.7800,82.0500,
     "https://upload.wikimedia.org/wikipedia/commons/7/7a/Draksharamam_Temple.jpg"),

    # Nellore
    ("Mypadu Beach","Nellore","beach",4.3,400,"summer",14.6330,80.2040,
     "https://upload.wikimedia.org/wikipedia/commons/8/8b/Mypadu_Beach.jpg"),
    ("Pulicat Lake","Nellore","nature",4.4,500,"winter",13.6500,80.3200,
     "https://upload.wikimedia.org/wikipedia/commons/9/9c/Pulicat_Lake.jpg"),

    # Srikakulam
    ("Arasavalli Sun Temple","Srikakulam","religious",4.6,300,"summer",18.3000,83.9000,
     "https://upload.wikimedia.org/wikipedia/commons/a/a1/Arasavalli_Sun_Temple.jpg"),
    ("Kalingapatnam Beach","Srikakulam","beach",4.2,400,"summer",18.3400,84.1200,
     "https://upload.wikimedia.org/wikipedia/commons/b/b2/Kalingapatnam_Beach.jpg"),

    # Vizianagaram
    ("Bobbili Fort","Vizianagaram","historical",4.2,300,"winter",18.5700,83.3500,
     "https://upload.wikimedia.org/wikipedia/commons/c/c3/Bobbili_Fort.jpg"),
    ("Ramatheertham Temple","Vizianagaram","religious",4.4,300,"summer",18.1800,83.4200,
     "https://upload.wikimedia.org/wikipedia/commons/d/d4/Ramatheertham_Temple.jpg"),

    # Eluru
    ("Kolleru Lake","Eluru","nature",4.4,800,"monsoon",16.6300,81.2000,
     "https://upload.wikimedia.org/wikipedia/commons/e/e2/Kolleru_Lake.jpg"),
    ("Dwaraka Tirumala Temple","Eluru","religious",4.6,400,"summer",16.9200,81.4500,
     "https://upload.wikimedia.org/wikipedia/commons/f/f3/Dwaraka_Tirumala_Temple.jpg"),

    # Bapatla
    ("Suryalanka Beach","Bapatla","beach",4.5,500,"summer",15.8300,80.5500,
     "https://upload.wikimedia.org/wikipedia/commons/g/g4/Suryalanka_Beach.jpg"),   
]
def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS destinations (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            city VARCHAR(100),
            category VARCHAR(100),
            rating FLOAT,
            estimated_cost INTEGER,
            season VARCHAR(50),
            latitude FLOAT,
            longitude FLOAT,
            image_url TEXT
        )
    """)
    conn.commit()
    conn.close()

def seed_database():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM destinations")
    for place in places_data:
        cursor.execute("""
            INSERT INTO destinations
            (name, city, category, rating, estimated_cost, season, latitude, longitude, image_url)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, place)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    seed_database()
    print("Database seeded successfully with extended Andhra Pradesh destinations!")