from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


dataset = {
    'Alice': {'Inception': 5, 'The Matrix': 3},
    'Bob': {'Inception': 4, 'The Matrix': 5},
    'Charlie': {'Inception': 3, 'The Matrix': 4}
}

df = pd.DataFrame(dataset).T.fillna(0)

# calculate cosine similarity
similarity = cosine_similarity(df)

# create DataFrame with similarity scores
similarity_df = pd.DataFrame(similarity, index=df.index, columns=df.index)

def get_similar_users(user):
    # get similar users
    similar_users = similarity_df[user].sort_values(ascending=False)
    
    # remove user from results
    similar_users = similar_users.drop(user)
    
    return similar_users

def get_recommendations(user):
    # get similar users
    similar_users = get_similar_users(user)
    
    # get movies rated by similar users but not by user
    recommendations = []
    
    for u in similar_users.index:
        for m in df.columns:
            if df.loc[u,m] > 0 and df.loc[user,m] == 0:
                recommendations.append(m)
                
    return recommendations

print(get_recommendations('Alice'))