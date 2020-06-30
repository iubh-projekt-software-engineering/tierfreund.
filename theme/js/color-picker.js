class ColorPicker {
    constructor(root) {
        this.root = root;
        this.activeColor = null;
        this.input = root.querySelector('input');
        this.colors = Array.from(
            this.root.querySelectorAll('.color')
        );
        this.init();
    }

    onClick(color) {
        const attrColor = color.getAttribute('data-color');
        
        if (color === this.activeColor) {
            color.classList.remove('is--active');
            this.activeColor = null;
        } else if (this.activeColor === null) {
            this.activeColor = color;
            color.classList.add('is--active');
        } else {
            this.activeColor.classList.remove('is--active');
            this.activeColor = color;
            color.classList.add('is--active');
        }

        this.input.value = this.activeColor === null ? null : attrColor;
    }

    init() {
        this.colors.forEach((color) => {
            color.addEventListener('click', () => {
                this.onClick(color);
            })
        });
    }
};

export default ColorPicker