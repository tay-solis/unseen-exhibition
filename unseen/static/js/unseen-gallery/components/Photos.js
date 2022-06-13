import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

import Photo from './Photo';

axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";

function Photos(props) {
  const [photos, setPhotos] = useState([]);
  const [error, setError] = useState("");
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    axios
      .get("/gallery/api/")
      .then((response) => setPhotos(response.data))
      .catch((err) => setError(err))
      .finally(() => setLoaded(true));
  });

  let photoComponents = photos.map((photo, i)=>{
    return (
      <Link to={`/gallery/${photo.slug}/`}>
        <Photo photo={photo} key={i}/>
      </Link>)
  })

  return (
    <section className="gallery__photos">
      {/* Error: {error}
      Loaded: {loaded} */}
      {!loaded && 
        <p>loading...</p>
      }
      {/* <div className="g-photo g-photo--empty">_</div> */}
      {photoComponents}
      {/* <div className="g-photo g-photo--empty">_</div> */}
    </section>
  );
}

export default Photos;
