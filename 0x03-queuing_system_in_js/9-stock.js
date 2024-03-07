#!/usr/bin/node

import express from 'express';
import utils from 'util'
import { createClient } from 'redis'

const PORT = 1245;
const app = express();
const client = createClient()
  .on('error', (err) => console.log(`Connection to redis failed with ${err}`))
  .on('connect', () => console.log('Redis client connect'));

const listProducts = [
  {id: 1, name: 'Suitcase 250', price: 50, stock: 4},
  {id: 2, name: 'Suitcase 450', price: 100, stock: 10},
  {id: 3, name: 'Suitcase 650', price: 350, stock: 2},
  {id: 4, name: 'Suitcase 1050', price: 550, stock: 5}
]

function getItemById(id) {
  return listProducts.find((item) => item.id === id);
}

function reserveStockById(itemId, stock) {
  client.set(itemId, stock);
}

async function getCurrentReservedStockById(itemId) {
  return await utils.promisify(client.GET).bind(client)(itemId);
}

app.get('/list_products', (req, res) => {
  const listProductsJson = listProducts.map((item) => {
    return {'itemId': item.id, 'itemName': item.name, 'price': item.price, 'initialAvailableQuantity': item.stock}
  });
  res.status(200).json(listProductsJson);
})

app.get('/list_products/:itemId', async (req, res) => {
  const item = getItemById(parseInt(req.params.itemId));

  if (!item) {
    res.status(404).json({status: 'Product not found'})
  }
  const itemJson = {itemId: item.id, itemName: item.name,
    price: item.price, initialAvailableQuantity: item.stock, currentQuantity: (item.stock - await getCurrentReservedStockById(item.id) || 0)}

  res.status(200).json(itemJson);
})

app.get('/reserve_product/:itemId', async (req, res) => {
  const item = getItemById(parseInt(req.params.itemId));

  if (item) {
    const reserved = parseInt(await getCurrentReservedStockById(parseInt(req.params.itemId)) || 0);

    const currentQuantity = item.stock - reserved;

    if (!currentQuantity || currentQuantity < 0) {
      res.status(200).json({status: "Not enough stock available", "itemId": parseInt(req.params.itemId)});
    } else {
      reserveStockById(req.params.itemId, reserved + 1);
      res.status(200).json({status: "Reservation confirmed", "itemId": parseInt(req.params.itemId)});
    }
  } else {
    res.status(404).json({"status": "Product not found"});
  }
})

app.listen(PORT, () => console.log(`Server listening on ${PORT}`));
