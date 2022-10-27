import { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'


function App() {

  const [products, setProduct] = useState([])
  const [shoppingcart, setShoppingCart] = useState([])

  const initialValue = 0;
  const sumWithInitial = shoppingcart.reduce(
    (previousValue, product) => previousValue + Number(product.value),
    initialValue
  );

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
        <li key={product.id} className="product">
          <img src={product.picture} alt="" className='images'/>
          <p>
          {product.name}
          </p>
          <p>
          R$ {product.value}
          </p>
          <button onClick={()=>addProductShoppingCart(product)}>Adicionar ao carrinho</button>
        </li>
      ))}   
      </ol>
      <hr />
      <h3>Carrinho R$ {sumWithInitial.toFixed(2)}</h3>
      <ol>
      {shoppingcart.map((product)=>(
        <li key={product.id}>
          {product.name}
          {}
        </li>
      ))}
      </ol>
    </>
  )
}

export default App
