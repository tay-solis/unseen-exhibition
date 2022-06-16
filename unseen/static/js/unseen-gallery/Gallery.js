import React, { useState, useEffect } from "react";
import axios from "axios";

import Photos from "./components/Photos";

axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";

const NUM_SHOW = 3;

function Gallery(props) {
  const [photos, setPhotos] = useState([]);
  const [error, setError] = useState("");
  const [loaded, setLoaded] = useState(false);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [length, setLength] = useState(photos.length);
  const show = NUM_SHOW;

  useEffect(() => {
    axios
      .get("/gallery/api/")
      .then((response) => {
        setPhotos(response.data);
        setLength(response.data.length);
      })
      .catch((err) => setError(err))
      .finally(() => setLoaded(true));
  }, []);

  const next = () => {
    if (currentIndex < length - show) {
      setCurrentIndex((prevState) => prevState + 1);
    }
  };

  const prev = () => {
    if (currentIndex > 0) {
      setCurrentIndex((prevState) => prevState - 1);
    }
  };

  return (
    <div className="gallery__container">
      <div className="gallery__photos-wrapper">
        <Photos currentIndex={currentIndex} photos={photos} show={show} />
      </div>
      <section className="gallery__controls">
        <button
          className="control-button control-button--gallery"
          onClick={prev}
        >
          <span className="icon icon--control-button icon--previous-gallery" />
          <span className="control-button__text">Previous</span>
        </button>
        <button
          className="control-button control-button--gallery"
          onClick={next}
        >
          <span className="control-button__text">Next</span>
          <span className="icon icon--control-button icon--next icon--next-gallery" />
        </button>
      </section>

      <section className="gallery__continue">
        <a href="/conversation/">
          <button className="button gallery__continue-button">Continue</button>
        </a>
      </section>
    </div>
  );
}

export default Gallery;
