import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
def collaborative_recommendations(user_id, ratings_df, destinations_df):

    user_item = ratings_df.pivot_table(
        index="user_id",
        columns="destination_id",
        values="rating"
    ).fillna(0)

    similarity = cosine_similarity(user_item)

    similarity_df = pd.DataFrame(
        similarity,
        index=user_item.index,
        columns=user_item.index
    )

    similar_users = similarity_df[user_id].sort_values(ascending=False)[1:3]

    recommended = []

    for sim_user in similar_users.index:
        user_data = ratings_df[ratings_df["user_id"] == sim_user]

        for dest in user_data["destination_id"]:
            if dest not in ratings_df[ratings_df["user_id"] == user_id]["destination_id"].values:
                recommended.append(dest)

    return destinations_df[destinations_df["id"].isin(recommended)].to_dict(orient="records")