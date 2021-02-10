const preOrder = node => {
    const arr = [];

    const traverse = node => {
        if(node) {
          arr.push(node.data);
          traverse(node.left);
          traverse(node.right);
        }
    };
    traverse(node);
    return arr;
};

const inOrder = node => {
    const arr = [];

    const traverse = node => {
        if(node) {
          traverse(node.left);
          arr.push(node.data);
          traverse(node.right);
        }
    };
    traverse(node);
    return arr;
};

const postOrder = node => {
    const arr = [];

    const traverse = node => {
        if(node) {
          traverse(node.left);
          traverse(node.right);
          arr.push(node.data);
        }
    };
    traverse(node);
    return arr;
};