import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

import { useParams } from "react-router-dom";

axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";

function FullScreenPhoto(props) {
  let { slug } = useParams();
  const [photo, setPhoto] = useState({});
  const [error, setError] = useState("");
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    axios
      .get(`/gallery/api/${slug}/`)
      .then((response) => setPhoto(response.data))
      .catch((err) => setError(err))
      .finally(() => setLoaded(true));
  });

  return (
    <div className="fs-photo">
      {!loaded && <p>loading...</p>}
      <section className="fs-photo__control-wrapper">
        <Link className="link--unstyled" to={`/gallery/`}>
          <button className="control-button control-button--fs control-button--close-fs">
            <span className="icon icon--control-button icon--close-fs" />
            <span className="control-button__text">Back</span>
          </button>
        </Link>

        <div className="fs-photo__controls">
          <button className="control-button control-button--fs control-button--previous-fs">
            <span className="icon icon--control-button icon--previous-fs" />
            <span className="control-button__text">Previous</span>
          </button>
          <button className="control-button control-button--fs control-button--next-fs">
            <span className="control-button__text">Next</span>
            <span className="icon icon--control-button icon--next icon--next-fs" />
          </button>
        </div>
      </section>
      <div className="fs-photo__wrapper">
        <img className="fs-photo__image" src={`${photo.photo}`} />
        <div className="fs-photo__info-wrapper">
          <a href={`/gallery/${photo.slug}/conversation/`}>
            <button className="button button--fs">View Responses</button>
          </a>
          <div className="fs-photo__info">
            <h2 className="fs-photo__title">{photo.name}</h2>
            {photo.description && (
              <p className="fs-photo__description">{photo.description}</p>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default FullScreenPhoto;
