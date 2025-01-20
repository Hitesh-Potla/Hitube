"use client";
import React from "react";
import { Header } from "@/components/header";
import { Sidebar } from "@/components/sidebar";
import VideoCard from "@/components/video-card";

const App = () => {
  return (
    <div>
      <Header />
      <div className="flex">
        <Sidebar />
        <div className="video-cards flex flex-wrap">
          <VideoCard />
          <VideoCard />
          <VideoCard />
          <VideoCard />
        </div>
      </div>
    </div>
  );
};

export default App;
