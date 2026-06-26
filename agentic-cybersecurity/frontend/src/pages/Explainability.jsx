import { useEffect, useState } from "react";
import API from "../services/api";

function Explainability() {
  const [loading, setLoading] = useState(true);

  const [images, setImages] = useState({
    shap: "",
    shapBar: "",
    lime: "",
    featureImportance: "",
    permutationImportance: "",
    roc: "",
    confusionMatrix: "",
  });

  const loadExplainability = async () => {
    setLoading(true);

    try {
      const [
        shap,
        shapBar,
        lime,
        featureImportance,
        permutationImportance,
        roc,
        confusionMatrix,
      ] = await Promise.all([
        API.get("/api/shap"),
        API.get("/api/shap-bar"),
        API.get("/api/lime"),
        API.get("/api/feature-importance"),
        API.get("/api/permutation-importance"),
        API.get("/api/roc"),
        API.get("/api/confusion-matrix"),
      ]);

      setImages({
        shap: shap.data.image,

        shapBar: shapBar.data.image,

        lime: lime.data.image,

        featureImportance: featureImportance.data.image,

        permutationImportance: permutationImportance.data.image,

        roc: roc.data.image,

        confusionMatrix: confusionMatrix.data.image,
      });
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadExplainability();
  }, []);

  if (loading) return <h2>Loading Explainability Dashboard...</h2>;

  const renderCard = (
    title,

    description,

    image
  ) => (
    <div
      style={{
        background: "#111827",

        borderRadius: "12px",

        padding: "20px",

        marginBottom: "20px",

        border: "1px solid #334155",
      }}
    >
      <h2>{title}</h2>

      <p
        style={{
          color: "#d1d5db",
          marginBottom: "15px",
        }}
      >
        {description}
      </p>

      {image ? (
        <>
          <img
            src={image}
            alt={title}
            width="100%"
            style={{
              cursor: "pointer",

              borderRadius: "8px",

              transition: "0.3s",
            }}
            onClick={() => window.open(image)}
          />

          <br />
          <br />

          <a href={image} download>
            <button>Download Image</button>
          </a>
        </>
      ) : (
        <div
          style={{
            height: "250px",

            display: "flex",

            alignItems: "center",

            justifyContent: "center",

            border: "1px dashed gray",

            borderRadius: "8px",
          }}
        >
          Not Generated
        </div>
      )}
    </div>
  );

  return (
    <div>
      <div
        style={{
          display: "flex",

          justifyContent: "space-between",

          alignItems: "center",

          marginBottom: "20px",
        }}
      >
        <h1>Explainable AI Dashboard</h1>

        <button onClick={loadExplainability}>Refresh</button>
      </div>

      {/* Summary */}

      <div
        style={{
          display: "grid",

          gridTemplateColumns: "repeat(4,1fr)",

          gap: "15px",

          marginBottom: "25px",
        }}
      >
        <div className="metric-card">
          SHAP
          <br />
          {images.shap ? "Generated" : "Pending"}
        </div>

        <div className="metric-card">
          LIME
          <br />
          {images.lime ? "Generated" : "Pending"}
        </div>

        <div className="metric-card">
          ROC
          <br />
          {images.roc ? "Generated" : "Pending"}
        </div>

        <div className="metric-card">
          Confusion Matrix
          <br />
          {images.confusionMatrix ? "Generated" : "Pending"}
        </div>
      </div>

      <div
        style={{
          display: "grid",

          gridTemplateColumns: "repeat(auto-fit,minmax(500px,1fr))",

          gap: "20px",
        }}
      >
        {renderCard(
          "SHAP Summary Plot",

          "Shows global feature importance and how each feature influences the prediction.",

          images.shap
        )}

        {renderCard(
          "SHAP Feature Ranking",

          "Ranks features according to their average SHAP values.",

          images.shapBar
        )}

        {renderCard(
          "LIME Local Explanation",

          "Explains an individual prediction by approximating the model locally.",

          images.lime
        )}

        {renderCard(
          "Feature Importance",

          "Displays model feature importance calculated during training.",

          images.featureImportance
        )}

        {renderCard(
          "Permutation Importance",

          "Measures feature importance by shuffling each feature and observing performance degradation.",

          images.permutationImportance
        )}

        {renderCard(
          "ROC Curve",

          "Illustrates True Positive Rate versus False Positive Rate for different thresholds.",

          images.roc
        )}

        {renderCard(
          "Confusion Matrix",

          "Shows True Positives, False Positives, True Negatives and False Negatives.",

          images.confusionMatrix
        )}
      </div>
    </div>
  );
}

export default Explainability;