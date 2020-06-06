class Stepmation {
  constructor(root, options = {}, items = null) {
    this.root = root;
    this.defaults = {
      index: 0,
      activeClass: 'stepmation--active',
      containerAttribute: 'data-stepmation-container',
      itemAttribute: 'data-stepmation-item',
    };
    this.config = Object.assign(this.defaults, options);
    this.subscriber = {};
    
    this.items = items;
  }

  to(index) {
    const oldIndex = this.index; // save old index    

    if (this.items === null) {
      console.error('There are no items to step on.');
      return;
    }

    if (index > this.items.length || index < 0) {
      console.error('Index out of bounds.');
      return;
    }

    this.index = index; // set new index 
    
    if (oldIndex === undefined) { // wasnt init yet
      this._in(this.index);
    } else {
      this._out(oldIndex, this.index);
    }

  }

  next() {
    this.to((this.index + 1));
  }

  previous() {
    this.to((this.index - 1));
  }

  collectContainer() {
    return []
      .slice
      .call(this.root.querySelectorAll(`[${this.config.containerAttribute}]`));
  }

  collectItems(container) {
    return (
      container.getAttribute(this.config.itemAttribute) !== null 
        ? [container]
        : [])
      .concat([].slice.call(container.querySelectorAll(`[${this.config.itemAttribute}]`)));
  }

  _animate(index, mode, onEnd) {
    const containerItem = this.items[index];    
    const itemsToAnimate = this.collectItems(containerItem);
    let count = itemsToAnimate.length;
    const _this = this;

    function waitTillEnd() {      
      count -= 1;
      if (count === 0) {
        _this._publish(`${mode}.after`, containerItem, itemsToAnimate);
        if (onEnd) {
          onEnd();
        }
      }
      this.removeEventListener('transitionend', waitTillEnd);
    };
    
    this._publish(`${mode}.before`, containerItem);

    // TODO: Dirty but current solution to work with setTimeout
    setTimeout(() => {
      itemsToAnimate.forEach((el) => {
        if (mode === 'in') {
          el.classList.add(this.config.activeClass);
        } else {
          el.classList.remove(this.config.activeClass);
        }
        el.addEventListener('transitionend', waitTillEnd.bind(el));
      });
    });
  }

  _in(index) {
    this._animate(index, 'in');
  }

  _out(oldindex, index) {
    this._animate(oldindex, 'out', () => {
      this._in(index);
    });
  }

  init() {
    if (this.items === null) {
      this.items = this.collectContainer();
    }
    
    this.to(this.config.index);
  }

  subscribe(event, callback) {
    if (event in this.subscriber) {
      this.subscriber[event].add(callback);
    } else {
      this.subscriber[event] = [callback];
    }
  }

  _publish(event, ...contextItems) {
    
    if (!(event in this.subscriber)) {
      return;
    }

    this.subscriber[event].forEach((callback) => {
      callback(this, ...contextItems);
    });
  }
}

export default Stepmation;