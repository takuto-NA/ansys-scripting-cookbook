import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Ansys Scripting Cookbook',
  description: 'Ansys製品（Workbench, Mechanical, SpaceClaim）の自動化に必要な実用的なスクリプトと開発ノウハウ',
  lang: 'ja',
  base: '/ansys-scripting-cookbook/',
  ignoreDeadLinks: true,
  
  themeConfig: {
    nav: [
      { text: 'ホーム', link: '/' },
      { text: 'ドキュメント', link: '/docs/' },
      { text: 'Mechanical', link: '/mechanical/' },
      { text: 'SpaceClaim', link: '/spaceclaim/' },
      { text: 'Workbench', link: '/workbench/' },
      { text: 'サンプル', link: '/examples/' }
    ],

    sidebar: {
      '/docs/': [
        {
          text: 'ガイド',
          items: [
            { text: 'クイックスタート', link: '/docs/quickstart' },
            { text: '用語集', link: '/docs/glossary' },
            { text: 'トラブルシューティング', link: '/docs/troubleshooting' },
            { text: '環境構築', link: '/docs/setup' }
          ]
        },
        {
          text: 'リファレンス',
          items: [
            { text: 'API 概要', link: '/docs/reference/api-overview' },
            { text: 'スクリプトテンプレート', link: '/docs/reference/script-template' },
            { text: 'デバッグガイド', link: '/docs/reference/debugging' },
            { text: '技術的な落とし穴', link: '/docs/reference/pitfalls' },
            { text: 'CAD 互換性', link: '/docs/reference/cad-compatibility' }
          ]
        },
        {
          text: '逆引き',
          items: [
            { text: 'チートシート', link: '/docs/cheatsheet' }
          ]
        }
      ],

      '/mechanical/': [
        {
          text: 'Mechanical スクリプト',
          items: [
            { text: '概要', link: '/mechanical/' },
            { text: 'ジオメトリ', link: '/mechanical/geometry/' },
            { text: 'メッシュ', link: '/mechanical/mesh/' },
            { text: '境界条件', link: '/mechanical/boundary-cond/' },
            { text: '後処理', link: '/mechanical/post-processing/' }
          ]
        }
      ],

      '/spaceclaim/': [
        {
          text: 'SpaceClaim スクリプト',
          items: [
            { text: '概要', link: '/spaceclaim/' },
            { text: 'モデリング', link: '/spaceclaim/modeling/' },
            { text: 'Named Selection', link: '/spaceclaim/named-selection/' }
          ]
        }
      ],

      '/workbench/': [
        {
          text: 'Workbench Journal',
          items: [
            { text: '概要', link: '/workbench/' },
            { text: '基本操作', link: '/workbench/basic-ops/' },
            { text: 'プロジェクト更新', link: '/workbench/project-update/' }
          ]
        }
      ],

      '/interop/': [
        {
          text: 'ツール間連携',
          items: [
            { text: '概要', link: '/interop/' },
            {
              text: 'STEP Import Tricks',
              items: [
                { text: 'Color to Named Selection', link: '/interop/step-import-trick/color_named_selection' }
              ]
            },
            {
              text: 'Workbench to Mechanical',
              items: [
                { text: 'Pass Parameters', link: '/interop/wb-to-mech/pass_parameters' }
              ]
            }
          ]
        }
      ],

      '/examples/': [
        {
          text: '統合サンプル',
          items: [
            { text: '概要', link: '/examples/' },
            { text: 'Rhino to CDB Workflow', link: '/examples/rhino_to_cdb_workflow' },
            { text: 'Rhino to Analysis Pipeline', link: '/examples/rhino_to_analysis_pipeline' }
          ]
        }
      ],

      '/common-snippets/': [
        {
          text: '共通スニペット',
          items: [
            { text: '概要', link: '/common-snippets/' }
          ]
        }
      ],

      '/': [
        {
          text: 'はじめに',
          items: [
            { text: 'ホーム', link: '/' },
            { text: 'クイックスタート', link: '/docs/quickstart' },
            { text: '用語集', link: '/docs/glossary' }
          ]
        },
        {
          text: 'カテゴリ',
          items: [
            { text: 'Mechanical', link: '/mechanical/' },
            { text: 'SpaceClaim', link: '/spaceclaim/' },
            { text: 'Workbench', link: '/workbench/' },
            { text: 'ツール間連携', link: '/interop/' },
            { text: 'サンプル', link: '/examples/' },
            { text: '共通スニペット', link: '/common-snippets/' }
          ]
        }
      ]
    },

    socialLinks: [
      {
        icon: 'github',
        link: 'https://github.com/your-org/ansys-scripting-cookbook'
      }
    ],

    search: {
      provider: 'local'
    },

    footer: {
      message: 'MIT License',
      copyright: 'Copyright © 2024 Ansys Scripting Cookbook'
    }
  }
})

