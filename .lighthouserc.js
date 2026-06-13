'use strict';
module.exports = {
  ci: {
    collect: {
      staticDistDir: '.',
      numberOfRuns: 1,
    },
    assert: {
      assertMatrix: [
        {
          // Home page — full quality bar.
          matchingUrlPattern: '.*/index\\.html$',
          assertions: {
            'categories:performance':    ['warn',  { minScore: 0.9 }],
            'categories:accessibility':  ['error', { minScore: 0.9 }],
            'categories:best-practices': ['warn',  { minScore: 0.9 }],
            'categories:seo':            ['error', { minScore: 0.9 }],
          },
        },
        {
          // 404 is intentionally noindex, so its SEO score is low by
          // design — hold it only to the accessibility bar.
          matchingUrlPattern: '.*/404\\.html$',
          assertions: {
            'categories:accessibility':  ['error', { minScore: 0.9 }],
          },
        },
      ],
    },
  },
};
