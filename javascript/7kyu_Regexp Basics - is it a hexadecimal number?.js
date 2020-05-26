String.prototype.hexNumber = function() {
  return /^(0x)?[0-9A-F]+$/i.test(this);
};