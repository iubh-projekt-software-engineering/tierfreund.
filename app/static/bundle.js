/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 0);
/******/ })
/************************************************************************/
/******/ ({

/***/ "./node_modules/@babel/runtime/helpers/classCallCheck.js":
/*!***************************************************************!*\
  !*** ./node_modules/@babel/runtime/helpers/classCallCheck.js ***!
  \***************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

eval("function _classCallCheck(instance, Constructor) {\n  if (!(instance instanceof Constructor)) {\n    throw new TypeError(\"Cannot call a class as a function\");\n  }\n}\n\nmodule.exports = _classCallCheck;\n\n//# sourceURL=webpack:///./node_modules/@babel/runtime/helpers/classCallCheck.js?");

/***/ }),

/***/ "./node_modules/@babel/runtime/helpers/createClass.js":
/*!************************************************************!*\
  !*** ./node_modules/@babel/runtime/helpers/createClass.js ***!
  \************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

eval("function _defineProperties(target, props) {\n  for (var i = 0; i < props.length; i++) {\n    var descriptor = props[i];\n    descriptor.enumerable = descriptor.enumerable || false;\n    descriptor.configurable = true;\n    if (\"value\" in descriptor) descriptor.writable = true;\n    Object.defineProperty(target, descriptor.key, descriptor);\n  }\n}\n\nfunction _createClass(Constructor, protoProps, staticProps) {\n  if (protoProps) _defineProperties(Constructor.prototype, protoProps);\n  if (staticProps) _defineProperties(Constructor, staticProps);\n  return Constructor;\n}\n\nmodule.exports = _createClass;\n\n//# sourceURL=webpack:///./node_modules/@babel/runtime/helpers/createClass.js?");

/***/ }),

/***/ "./theme/index.scss":
/*!**************************!*\
  !*** ./theme/index.scss ***!
  \**************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

eval("module.exports = __webpack_require__.p + \"bundle.css\";\n\n//# sourceURL=webpack:///./theme/index.scss?");

/***/ }),

/***/ "./theme/js/color-picker.js":
/*!**********************************!*\
  !*** ./theme/js/color-picker.js ***!
  \**********************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _babel_runtime_helpers_classCallCheck__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @babel/runtime/helpers/classCallCheck */ \"./node_modules/@babel/runtime/helpers/classCallCheck.js\");\n/* harmony import */ var _babel_runtime_helpers_classCallCheck__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_babel_runtime_helpers_classCallCheck__WEBPACK_IMPORTED_MODULE_0__);\n/* harmony import */ var _babel_runtime_helpers_createClass__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @babel/runtime/helpers/createClass */ \"./node_modules/@babel/runtime/helpers/createClass.js\");\n/* harmony import */ var _babel_runtime_helpers_createClass__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_babel_runtime_helpers_createClass__WEBPACK_IMPORTED_MODULE_1__);\n\n\n\nvar ColorPicker = /*#__PURE__*/function () {\n  function ColorPicker(root) {\n    _babel_runtime_helpers_classCallCheck__WEBPACK_IMPORTED_MODULE_0___default()(this, ColorPicker);\n\n    this.root = root;\n    this.activeColor = null;\n    this.input = root.querySelector('input');\n    this.colors = Array.from(this.root.querySelectorAll('.color'));\n    this.init();\n  }\n\n  _babel_runtime_helpers_createClass__WEBPACK_IMPORTED_MODULE_1___default()(ColorPicker, [{\n    key: \"onClick\",\n    value: function onClick(color) {\n      var attrColor = color.getAttribute('data-color');\n\n      if (color === this.activeColor) {\n        color.classList.remove('is--active');\n        this.activeColor = null;\n      } else if (this.activeColor === null) {\n        this.activeColor = color;\n        color.classList.add('is--active');\n      } else {\n        this.activeColor.classList.remove('is--active');\n        this.activeColor = color;\n        color.classList.add('is--active');\n      }\n\n      this.input.value = this.activeColor === null ? null : attrColor;\n    }\n  }, {\n    key: \"init\",\n    value: function init() {\n      var _this = this;\n\n      this.colors.forEach(function (color) {\n        color.addEventListener('click', function () {\n          _this.onClick(color);\n        });\n      });\n    }\n  }]);\n\n  return ColorPicker;\n}();\n\n;\n/* harmony default export */ __webpack_exports__[\"default\"] = (ColorPicker);\n\n//# sourceURL=webpack:///./theme/js/color-picker.js?");

/***/ }),

/***/ "./theme/js/index.js":
/*!***************************!*\
  !*** ./theme/js/index.js ***!
  \***************************/
/*! no exports provided */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _stepmation__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./stepmation */ \"./theme/js/stepmation.js\");\n/* harmony import */ var _color_picker__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./color-picker */ \"./theme/js/color-picker.js\");\n\n\nArray.from(document.querySelectorAll('.js--color-picker')).forEach(function (el) {\n  new _color_picker__WEBPACK_IMPORTED_MODULE_1__[\"default\"](el);\n});\n\nif (document.querySelector('.onboarding--stage')) {\n  var myStepmation = new _stepmation__WEBPACK_IMPORTED_MODULE_0__[\"default\"](document.querySelector('.onboarding--stage'));\n  document.querySelector('.onboarding--stage_next').addEventListener('click', function () {\n    myStepmation.next();\n  });\n  myStepmation.subscribe('in.before', function (instance, container) {\n    container.style.display = 'block';\n  });\n  myStepmation.subscribe('out.after', function (instance, container) {\n    if (instance.index < 1) {\n      return;\n    }\n\n    instance.items[instance.index - 1].style.display = 'none';\n    [].slice.call(document.querySelectorAll('.onboarding--stage_step')).forEach(function (el, index) {\n      if (instance.index === index) {\n        el.classList.add('is--active');\n      } else {\n        el.classList.remove('is--active');\n      }\n    });\n  });\n  myStepmation.init();\n}\n\nArray.from(document.querySelectorAll('.js--password-toggler')).forEach(function (toggler) {\n  toggler.addEventListener('click', function () {\n    var inputField = toggler.previousElementSibling;\n    inputField.type = inputField.type === 'text' ? 'password' : 'text';\n  });\n});\nvar burger = document.querySelector('.burger');\nvar header = document.querySelector('.header');\nvar nav = document.querySelector('.navigation');\nburger.addEventListener('click', function () {\n  burger.classList.toggle('is--active');\n  nav.classList.toggle('is--active');\n  header.classList.toggle('is--active');\n});\n\n//# sourceURL=webpack:///./theme/js/index.js?");

/***/ }),

/***/ "./theme/js/stepmation.js":
/*!********************************!*\
  !*** ./theme/js/stepmation.js ***!
  \********************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _babel_runtime_helpers_classCallCheck__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @babel/runtime/helpers/classCallCheck */ \"./node_modules/@babel/runtime/helpers/classCallCheck.js\");\n/* harmony import */ var _babel_runtime_helpers_classCallCheck__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_babel_runtime_helpers_classCallCheck__WEBPACK_IMPORTED_MODULE_0__);\n/* harmony import */ var _babel_runtime_helpers_createClass__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @babel/runtime/helpers/createClass */ \"./node_modules/@babel/runtime/helpers/createClass.js\");\n/* harmony import */ var _babel_runtime_helpers_createClass__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_babel_runtime_helpers_createClass__WEBPACK_IMPORTED_MODULE_1__);\n\n\n\nvar Stepmation = /*#__PURE__*/function () {\n  function Stepmation(root) {\n    var options = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : {};\n    var items = arguments.length > 2 && arguments[2] !== undefined ? arguments[2] : null;\n\n    _babel_runtime_helpers_classCallCheck__WEBPACK_IMPORTED_MODULE_0___default()(this, Stepmation);\n\n    this.root = root;\n    this.defaults = {\n      index: 0,\n      activeClass: 'stepmation--active',\n      containerAttribute: 'data-stepmation-container',\n      itemAttribute: 'data-stepmation-item'\n    };\n    this.config = Object.assign(this.defaults, options);\n    this.subscriber = {};\n    this.items = items;\n  }\n\n  _babel_runtime_helpers_createClass__WEBPACK_IMPORTED_MODULE_1___default()(Stepmation, [{\n    key: \"to\",\n    value: function to(index) {\n      var oldIndex = this.index; // save old index    \n\n      if (this.items === null) {\n        console.error('There are no items to step on.');\n        return;\n      }\n\n      if (index > this.items.length || index < 0) {\n        console.error('Index out of bounds.');\n        return;\n      }\n\n      this.index = index; // set new index \n\n      if (oldIndex === undefined) {\n        // wasnt init yet\n        this._in(this.index);\n      } else {\n        this._out(oldIndex, this.index);\n      }\n    }\n  }, {\n    key: \"next\",\n    value: function next() {\n      this.to(this.index + 1);\n    }\n  }, {\n    key: \"previous\",\n    value: function previous() {\n      this.to(this.index - 1);\n    }\n  }, {\n    key: \"collectContainer\",\n    value: function collectContainer() {\n      return [].slice.call(this.root.querySelectorAll(\"[\".concat(this.config.containerAttribute, \"]\")));\n    }\n  }, {\n    key: \"collectItems\",\n    value: function collectItems(container) {\n      return (container.getAttribute(this.config.itemAttribute) !== null ? [container] : []).concat([].slice.call(container.querySelectorAll(\"[\".concat(this.config.itemAttribute, \"]\"))));\n    }\n  }, {\n    key: \"_animate\",\n    value: function _animate(index, mode, onEnd) {\n      var _this2 = this;\n\n      var containerItem = this.items[index];\n      var itemsToAnimate = this.collectItems(containerItem);\n      var count = itemsToAnimate.length;\n\n      var _this = this;\n\n      function waitTillEnd() {\n        count -= 1;\n\n        if (count === 0) {\n          _this._publish(\"\".concat(mode, \".after\"), containerItem, itemsToAnimate);\n\n          if (onEnd) {\n            onEnd();\n          }\n        }\n\n        this.removeEventListener('transitionend', waitTillEnd);\n      }\n\n      ;\n\n      this._publish(\"\".concat(mode, \".before\"), containerItem); // TODO: Dirty but current solution to work with setTimeout\n\n\n      setTimeout(function () {\n        itemsToAnimate.forEach(function (el) {\n          if (mode === 'in') {\n            el.classList.add(_this2.config.activeClass);\n          } else {\n            el.classList.remove(_this2.config.activeClass);\n          }\n\n          el.addEventListener('transitionend', waitTillEnd.bind(el));\n        });\n      });\n    }\n  }, {\n    key: \"_in\",\n    value: function _in(index) {\n      this._animate(index, 'in');\n    }\n  }, {\n    key: \"_out\",\n    value: function _out(oldindex, index) {\n      var _this3 = this;\n\n      this._animate(oldindex, 'out', function () {\n        _this3._in(index);\n      });\n    }\n  }, {\n    key: \"init\",\n    value: function init() {\n      if (this.items === null) {\n        this.items = this.collectContainer();\n      }\n\n      this.to(this.config.index);\n    }\n  }, {\n    key: \"subscribe\",\n    value: function subscribe(event, callback) {\n      if (event in this.subscriber) {\n        this.subscriber[event].add(callback);\n      } else {\n        this.subscriber[event] = [callback];\n      }\n    }\n  }, {\n    key: \"_publish\",\n    value: function _publish(event) {\n      var _this4 = this;\n\n      for (var _len = arguments.length, contextItems = new Array(_len > 1 ? _len - 1 : 0), _key = 1; _key < _len; _key++) {\n        contextItems[_key - 1] = arguments[_key];\n      }\n\n      if (!(event in this.subscriber)) {\n        return;\n      }\n\n      this.subscriber[event].forEach(function (callback) {\n        callback.apply(void 0, [_this4].concat(contextItems));\n      });\n    }\n  }]);\n\n  return Stepmation;\n}();\n\n/* harmony default export */ __webpack_exports__[\"default\"] = (Stepmation);\n\n//# sourceURL=webpack:///./theme/js/stepmation.js?");

/***/ }),

/***/ 0:
/*!****************************************************!*\
  !*** multi ./theme/index.scss ./theme/js/index.js ***!
  \****************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

eval("__webpack_require__(/*! ./theme/index.scss */\"./theme/index.scss\");\nmodule.exports = __webpack_require__(/*! ./theme/js/index.js */\"./theme/js/index.js\");\n\n\n//# sourceURL=webpack:///multi_./theme/index.scss_./theme/js/index.js?");

/***/ })

/******/ });