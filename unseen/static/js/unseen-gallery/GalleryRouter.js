import React from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import Gallery from "./Gallery";
import FullScreenPhoto from "./FullScreenPhoto";

export default function GalleryRouter() {
  return (
    <Router>
        <Routes>
          <Route path="/gallery/:slug" element={<FullScreenPhoto />}/>
          <Route path="/gallery/" element={<Gallery/>} />
        </Routes>
    </Router>
  );
}