"use client";
import React from "react";
import { Header } from "@/components/header";
import { Sidebar } from "@/components/sidebar";
// import VideoHome from "@/app/videoHome/page";

const App = () => {
  return (
    <div>
      <Header />
      <div className="flex">
        <Sidebar />
        <div className="video-cards flex flex-wrap"></div>
      </div>
    </div>
  );
};

export default App;
