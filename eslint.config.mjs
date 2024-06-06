import js from '@eslint/js';
import stylisticJs from '@stylistic/eslint-plugin-js';

export default {
  ...js.configs.recommended,
  'languageOptions': {
    'parserOptions': {
      'ecmaVersion': 2020
    }
  },
    'plugins': {
    '@stylistic/js': stylisticJs
  },
  'rules': {
    '@stylistic/js/max-len': ['error', { 'code': 120 }],
    'indent': ['error', 2],
    'linebreak-style': ['error', 'unix'],
    'quotes': ['error', 'single'],
    'semi': ['error', 'always']
  }
};
