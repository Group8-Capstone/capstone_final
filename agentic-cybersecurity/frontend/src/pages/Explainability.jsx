function Explainability() {

  return (

    <div>

      <h1>SHAP Explainability</h1>

      <img

        src="http://127.0.0.1:8000/outputs/explainability/shap/shap_summary.png"

        width="100%"
      />

      <br /><br />

      <h1>LIME Explainability</h1>

      <img

        src="http://127.0.0.1:8000/outputs/explainability/lime/lime_explanation.png"

        width="100%"
      />

    </div>
  )
}

export default Explainability