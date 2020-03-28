function profit(info) {
	const {costPrice, sellPrice, inventory} = info;
    return Math.round((sellPrice - costPrice)*inventory);
}


console.log(profit({
  costPrice: 32.67,
  sellPrice: 45.00,
  inventory: 1200
}));