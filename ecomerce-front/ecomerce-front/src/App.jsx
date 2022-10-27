import { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'

import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

function App() {

  const [products, setProduct] = useState([])
  const [shoppingcart, setShoppingCart] = useState([])

  useEffect(()=>{
    async function getProducts(){
      const response = await axios.get('http://localhost:8000/api/v1/products/')
      const list = response.data
      setProduct(list)
    }
    getProducts()
  }, [])

  function addProductShoppingCart(product){
    setShoppingCart([...shoppingcart, product])
  }
  return (
    <>
      <hr />
      <h2>listagem de produtos</h2>
      <ol>
      {products.map((product)=>(
        <li key={product.id}>
          <img src={product.picture} alt="" />
          <button onClick={()=>addProductShoppingCart(product)}>Adicionar ao carrinho</button>
        </li>
      ))}   
      </ol>
      <hr />
      <h3>Carrinho</h3>
      <ol>
      {shoppingcart.map((product)=>(
        <li key={product.id}>
          {product.name}
        </li>
      ))}
      </ol>
    </>
  )
}

export default App
