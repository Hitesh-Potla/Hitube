# import numpy as np
# from sklearn.preprocessing import MinMaxScaler
# from sklearn.metrics.pairwise import cosine_similarity
# from .models import *

# def get_video_recommendations(video_id, top_n=10):
#     try:
#         # Fetch all videos and the target video
#         videos = Video.objects.all()
#         target_video = videos.get(id=video_id)

#         # Prepare data for similarity calculation
#         data = []
#         video_ids = []
        
#         for video in videos:
#             tags = [tag.id for tag in video.tags.all()]
#             category = [video.category or ""]  # Convert None to empty string
#             features = [video.views, video.likes, video.upload_date.timestamp()] + tags + category
#             data.append(features)
#             video_ids.append(video.id)

#         # Normalize numerical features
#         scaler = MinMaxScaler()
#         data = scaler.fit_transform(data)

#         # Compute similarities
#         similarities = cosine_similarity([data[video_ids.index(target_video.id)]], data).flatten()

#         # Get top N similar videos (excluding the target video itself)
#         similar_indices = np.argsort(-similarities)[1:top_n + 1]
#         similar_videos = [videos[i] for i in similar_indices]

#         return similar_videos

#     except Exception as e:
#         print(f"Error in get_video_recommendations: {e}")
#         return []
# def get_recommendations(video_id, page=1, page_size=20):
#     recommendations = get_video_recommendations(video_id, top_n=page_size)
#     return recommendations
