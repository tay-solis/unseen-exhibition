import React, {useState, useEffect} from "react";
import axios from "axios";

import { useParams } from 'react-router-dom';

axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";

function FullScreenPhoto(props) {
  let { slug } = useParams();
  const [photo, setPhoto] = useState({});
  const [error, setError] = useState("");
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    axios
      .get(`/gallery/api/${slug}`)
      .then((response) => setPhoto(response.data))
      .catch((err) => setError(err))
      .finally(() => setLoaded(true));
  });

  return (
    <div className="fs-photo">
      {!loaded ? (
        <p>loading...</p>
      ) : (
        <div>
          <img className="fs-photo__image" src={`${photo.photo}`} />
          <div className="fs-photo__info">
            <h2 className="fs-photo__title">{photo.name}</h2>
            {photo.description && (
              <p className="fs-photo__description">{photo.description}</p>
            )}
            {photo.url && (
                <p className="fs-photo__description">See Full Work</p>
            )}
          </div>
        </div>
      )}
    </div>
  );
}

export default FullScreenPhoto;
