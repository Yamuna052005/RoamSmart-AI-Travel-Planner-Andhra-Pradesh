import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def collaborative_recommendations(user_id, destinations, ratings, top_n=5):

    ratings_matrix = ratings.pivot_table(
        index="user_id",
        columns="destination_id",
        values="rating"
    ).fillna(0)

    user_similarity = cosine_similarity(ratings_matrix)

    similarity_df = pd.DataFrame(
        user_similarity,
        index=ratings_matrix.index,
        columns=ratings_matrix.index
    )

    if user_id not in similarity_df.index:
        return []

    similar_users = similarity_df[user_id].sort_values(ascending=False)[1:6].index

    similar_users_ratings = ratings[
        ratings["user_id"].isin(similar_users)
    ]

    recommended_dest_ids = (
        similar_users_ratings
        .groupby("destination_id")["rating"]
        .mean()
        .sort_values(ascending=False)
        .head(top_n)
        .index
    )

    recommendations = destinations[
        destinations["id"].isin(recommended_dest_ids)
    ]

    return recommendations.to_dict(orient="records")