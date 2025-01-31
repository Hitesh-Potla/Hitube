"use client";
import React, { useEffect, useState } from "react";
import { Header } from "@/components/header";
import { Sidebar } from "@/components/sidebar";

interface Video {
  id: number;
  title: string;
  thumbnail: string;
  video_file: string;
  uploaded_by: string;
  comments_count: number;
  upload_date: string;
  views: number;
  likes: number;
  is_liked: boolean;
}

const App = () => {
  const [videos, setVideos] = useState<Video[]>([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/videos/")
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          setVideos(data.videos);
        }
      })
      .catch((error) => console.error("Error fetching videos:", error));
  }, []);

  return (
    <div>
      <Header />
      <div className="flex">
        <Sidebar />

        {videos.map((video) => (
          <div key={video.id} className="video-card">
            {/* <img
              src={video.thumbnail}
              alt={video.title}
              className="w-full h-48 object-cover"
            /> */}
            <video
              autoPlay
              controls
              className="w-full h-48"
              src={video.video_file}
            ></video>
            <div className="p-2">
              <h3 className="text-lg font-medium">{video.title}</h3>
              <p className="text-sm text-gray-600">
                {video.uploaded_by} • {video.views} views • {video.upload_date}
              </p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default App;
