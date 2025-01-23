"use client";

import { Button } from "@/components/ui/button";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Separator } from "@/components/ui/separator";
import {
  Home,
  Play,
  Users,
  History,
  TrendingUpIcon as Trending,
  ShoppingBag,
  Music2,
  Film,
  Radio,
  Gamepad2,
  Newspaper,
  Trophy,
  GraduationCap,
  Shirt,
  Podcast,
  LayoutGrid,
} from "lucide-react";

export function Sidebar() {
  return (
    <ScrollArea className="w-60 flex-shrink-0 border-r h-[100vh]">
      <div className="py-2 px-2">
        <div className="space-y-1">
          <Button variant="ghost" className="w-full justify-start gap-4">
            <Home className="h-5 w-5" />
            Home
          </Button>
          <Button variant="ghost" className="w-full justify-start gap-4">
            <Users className="h-5 w-5" />
            Subscriptions
          </Button>
        </div>
        <Separator className="my-2" />
        <div className="space-y-1">
          <Button variant="ghost" className="w-full justify-start gap-4">
            <History className="h-5 w-5" />
            History
          </Button>
        </div>
        <Separator className="my-2" />
        <div className="space-y-4">
          <div className="px-4 text-sm">
            Sign in to like videos, comment, and subscribe.
          </div>
          <a href="signin">
            <Button variant="outline" className="gap-2">
              Sign in
            </Button>
          </a>
        </div>
        <Separator className="my-2" />
        <div className="space-y-1">
          <div className="px-4 py-2 text-sm font-medium">Explore</div>

          <Button variant="ghost" className="w-full justify-start gap-4">
            <Radio className="h-5 w-5" />
            Live
          </Button>

          <Button variant="ghost" className="w-full justify-start gap-4">
            <Newspaper className="h-5 w-5" />
            News
          </Button>

          <Button variant="ghost" className="w-full justify-start gap-4">
            <GraduationCap className="h-5 w-5" />
            Courses
          </Button>

          <Button variant="ghost" className="w-full justify-start gap-4">
            <Podcast className="h-5 w-5" />
            Podcasts
          </Button>
          <Button variant="ghost" className="w-full justify-start gap-4">
            <LayoutGrid className="h-5 w-5" />
            Playlists
          </Button>
        </div>
      </div>
    </ScrollArea>
  );
}
