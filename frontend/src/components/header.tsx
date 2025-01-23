"use client";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Menu, Mic, Search, Upload, Bell, Moon, Sun } from "lucide-react";
import Image from "next/image";
import { useTheme } from "next-themes";

export function Header() {
  const { theme, setTheme } = useTheme();

  return (
    <header className="flex items-center justify-between gap-4 px-4 h-14 bg-background border-b">
      <div className="header-left flex items-center gap-4">
        <Button variant="ghost" size="icon" className="hover:bg-accent">
          <Menu className="h-10 w-10" />
        </Button>
        <div className="flex items-center gap-1">
          <Image
            src="/Logo.png"
            alt="YouTube"
            width={100}
            height={50}
            className="w-auto h-10"
          />
        </div>
      </div>
      <div className="flex flex-1 justify-center max-w-[732px]">
        <div className="flex w-full max-w-[638px]">
          <div className="flex flex-1">
            <Input
              type="search"
              placeholder="Search"
              className="rounded-l-full rounded-r-none border-r-0 focus-visible:ring-0 focus-visible:ring-offset-0"
            />
          </div>
          <Button
            variant="outline"
            size="icon"
            className="rounded-l-none rounded-r-full border-l-0"
          >
            <Search className="h-5 w-5" />
          </Button>
          <Button variant="ghost" size="icon" className="ml-2 hover:bg-accent">
            <Mic className="h-5 w-5" />
          </Button>
        </div>
      </div>
      <div className="flex items-center gap-2">
        <Button variant="ghost" size="icon" className="hover:bg-accent">
          <Upload className="h-5 w-5" />
        </Button>
        <Button variant="ghost" size="icon" className="hover:bg-accent">
          <Bell className="h-5 w-5" />
        </Button>
        <Button
          variant="ghost"
          size="icon"
          onClick={() => setTheme(theme === "dark" ? "light" : "dark")}
        >
          {theme === "dark" ? (
            <Sun className="h-5 w-5" />
          ) : (
            <Moon className="h-5 w-5" />
          )}
        </Button>
        <a href="/signup">
          <Button variant="outline" className="gap-2">
            Sign up
          </Button>
        </a>
      </div>
    </header>
  );
}
