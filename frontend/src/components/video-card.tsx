"use client";
import React from "react";

const VideoCard = () => {
  return (
    <div className="max-w-sm rounded overflow-hidden shadow-lg p-2">
      <img
        className="w-full rounded"
        src="thumnail.jpg"
        alt="Video Thumbnail"
      />
      <div className="px-6 py-1">
        <div className="title-part flex gap-6 items-center mb-2 mt-2">
          <img className="h-10 rounded-full w-10" src="logo.png" alt="" />
          <div className="font-bold text-xl mb-2">Video Title</div>
        </div>
        <h2 className="text-xs ml-16">Video Creator</h2>
      </div>
      <div className="px-6 ml-16">
        <span>10M .</span>
        <span> 1 hour ago</span>
      </div>
    </div>
  );
};

export default VideoCard;
