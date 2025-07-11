<template>
    <div class="property-estimator">
      <h2>Estimador de Precio de Propiedad</h2>
      <form @submit.prevent="calculatePrice">
        <div class="form-group">
          <label for="area">Área (m²)</label>
          <input v-model="area" type="number" id="area" required />
        </div>
        <div class="form-group">
          <label for="age">Antigüedad (años)</label>
          <input v-model="age" type="number" id="age" required />
        </div>
        <button type="submit">Estimar Precio</button>
      </form>
  
      <div v-if="estimatedPrice !== null" class="result">
        <h3>Precio Estimado: ${{ estimatedPrice }}</h3>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        area: null,
        age: null,
        estimatedPrice: null,
      };
    },
    methods: {
      calculatePrice() {
        // Lógica simple de estimación de precios (esto se puede mejorar)
        if (this.area && this.age) {
          // Simple cálculo basado en área y antigüedad
          this.estimatedPrice = this.area * 5000 - this.age * 1000;
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .property-estimator {
    max-width: 400px;
    margin: 0 auto;
  }
  .form-group {
    margin-bottom: 15px;
  }
  label {
    display: block;
    margin-bottom: 5px;
  }
  input {
    width: 100%;
    padding: 8px;
    margin-top: 5px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  button {
    background-color: #007BFF;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  button:hover {
    background-color: #0056b3;
  }
  .result {
    margin-top: 20px;
    font-size: 18px;
    font-weight: bold;
  }
  </style>
  