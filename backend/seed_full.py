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
        name TEXT,
        city TEXT,
        category TEXT,
        rating FLOAT,
        estimated_cost INT,
        season TEXT,
        latitude FLOAT,
        longitude FLOAT,
        image_url TEXT
    )
    """)

    conn.commit()
    conn.close()


# -------------------------------
# TOURISM DATA
# -------------------------------

places_data = [

("Tirumala Temple","Tirupati","religious",4.9,2000,"all",13.683,79.347,"https://picsum.photos/300"),
("Kapila Theertham","Tirupati","religious",4.5,500,"summer",13.628,79.419,"https://picsum.photos/301"),
("Talakona Waterfalls","Chittoor","nature",4.6,800,"monsoon",13.809,79.209,"https://picsum.photos/302"),
("Horsley Hills","Chittoor","hillstation",4.5,1500,"winter",13.650,78.400,"https://picsum.photos/303"),
("Sri Kalahasti Temple","Tirupati","religious",4.7,700,"all",13.749,79.698,"https://picsum.photos/304"),
("Chandragiri Fort","Tirupati","historical",4.5,600,"winter",13.585,79.318,"https://picsum.photos/305"),
("Nagalapuram Falls","Tirupati","nature",4.6,900,"monsoon",13.400,79.600,"https://picsum.photos/306"),

("Lepakshi Temple","Anantapur","historical",4.7,600,"winter",13.801,77.605,"https://picsum.photos/307"),
("Penukonda Fort","Anantapur","historical",4.3,400,"winter",14.080,77.590,"https://picsum.photos/308"),
("Puttaparthi Ashram","Anantapur","religious",4.6,500,"all",14.170,77.810,"https://picsum.photos/309"),

("Belum Caves","Kurnool","adventure",4.6,700,"summer",15.103,78.110,"https://picsum.photos/310"),
("Srisailam Temple","Kurnool","religious",4.8,1200,"winter",16.072,78.868,"https://picsum.photos/311"),
("Oravakallu Rock Garden","Kurnool","nature",4.4,600,"summer",15.780,78.050,"https://picsum.photos/312"),

("Gandikota Fort","Kadapa","historical",4.7,900,"winter",14.815,78.260,"https://picsum.photos/313"),

("Araku Valley","Visakhapatnam","nature",4.8,2500,"winter",18.333,82.867,"https://picsum.photos/314"),
("Borra Caves","Visakhapatnam","adventure",4.7,2000,"winter",18.283,83.040,"https://picsum.photos/315"),
("Rushikonda Beach","Visakhapatnam","beach",4.6,500,"summer",17.780,83.380,"https://picsum.photos/316"),
("Yarada Beach","Visakhapatnam","beach",4.6,500,"summer",17.659,83.260,"https://picsum.photos/317"),
("RK Beach","Visakhapatnam","beach",4.5,300,"summer",17.720,83.330,"https://picsum.photos/318"),

("Papikondalu","East Godavari","nature",4.8,2200,"winter",17.593,81.796,"https://picsum.photos/319"),
("Maredumilli","East Godavari","nature",4.7,1500,"winter",17.600,81.750,"https://picsum.photos/320"),

("Annavaram Temple","Kakinada","religious",4.7,900,"all",17.100,82.150,"https://picsum.photos/321"),

("Kolleru Lake","Eluru","nature",4.4,700,"winter",16.630,81.200,"https://picsum.photos/322"),

("Amaravati Stupa","Guntur","historical",4.6,600,"winter",16.572,80.357,"https://picsum.photos/323"),
("Undavalli Caves","Guntur","historical",4.5,500,"winter",16.500,80.580,"https://picsum.photos/324"),

("Kanaka Durga Temple","Vijayawada","religious",4.8,700,"all",16.506,80.648,"https://picsum.photos/325"),
("Prakasam Barrage","Vijayawada","landmark",4.4,300,"winter",16.506,80.648,"https://picsum.photos/326"),

("Manginapudi Beach","Machilipatnam","beach",4.4,400,"summer",16.166,81.133,"https://picsum.photos/327"),

("Pulicat Lake","Nellore","nature",4.4,500,"winter",13.650,80.320,"https://picsum.photos/328"),
("Mypadu Beach","Nellore","beach",4.3,400,"summer",14.633,80.204,"https://picsum.photos/329"),

("Arasavalli Sun Temple","Srikakulam","religious",4.7,300,"all",18.300,83.900,"https://picsum.photos/330"),

("Bobbili Fort","Vizianagaram","historical",4.2,300,"winter",18.570,83.350,"https://picsum.photos/331"),

("Antarvedi Beach","Konaseema","beach",4.4,700,"summer",16.333,81.733,"https://picsum.photos/332")

]


# -------------------------------
# AUTO GENERATE UNTIL 150
# -------------------------------

while len(places_data) < 150:
    i = len(places_data) + 1
    places_data.append((
        f"Andhra Tourist Spot {i}",
        "Andhra Pradesh",
        "nature",
        4.0,
        500,
        "winter",
        15.0 + (i/100),
        80.0 + (i/100),
        f"https://picsum.photos/{350+i}"
    ))


# -------------------------------
# INSERT DATA
# -------------------------------

def seed_database():

    conn = get_connection()
    cursor = conn.cursor()

    for place in places_data:
        cursor.execute("""
        INSERT INTO destinations
        (name, city, category, rating, estimated_cost, season, latitude, longitude, image_url)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, place)

    conn.commit()
    conn.close()

    print("150 Andhra Pradesh tourism places inserted successfully!")


# -------------------------------
# RUN PROGRAM
# -------------------------------

create_table()
seed_database()