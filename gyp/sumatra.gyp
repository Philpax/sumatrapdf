{
    'variables': {
        'nasm_dir': '../bin',
    },

    'includes': [
        'test_util.gyp',
        'common.gypi',
        'lzma.gyp',
        'libwebp.gyp',
        'djvu.gyp',
        'bzip2.gyp',
        'chmlib.gyp',
        'unarr.gyp',
        'mupdf.gyp',
        'mui.gyp',
    ],

    'targets': [
        {
            'target_name': 'SumatraPDF',
            'type': 'executable',
            'msvs_disabled_warnings': [4244],
            'dependencies': [
                "zlib",
                "lzma",
                "libwebp",
                "djvu",
                "bzip2",
                "chmlib",
                "utils",
                "unarr",
                'mupdf',
                'mui',
            ],
            'include_dirs': [
                "../src",
                "../ext/synctex",
            ],
            'sources': [
                "../src/AppPrefs.cpp",
                "../src/AppPrefs.h",
                "../src/AppTools.cpp",
                "../src/AppTools.h",
                "../src/AppUtil.cpp",
                "../src/AppUtil.h",
                "../src/BaseEngine.h",
                "../src/Canvas.cpp",
                "../src/Canvas.h",
                "../src/Caption.cpp",
                "../src/Caption.h",
                "../src/ChmDoc.cpp",
                "../src/ChmDoc.h",
                "../src/ChmModel.cpp",
                "../src/ChmModel.h",
                "../src/Controller.h",
                "../src/CrashHandler.cpp",
                "../src/CrashHandler.h",
                "../src/DisplayModel.cpp",
                "../src/DisplayModel.h",
                "../src/DjVuEngine.cpp",
                "../src/DjVuEngine.h",
                "../src/Doc.cpp",
                "../src/Doc.h",
                "../src/EbookBase.h",
                "../src/EbookController.cpp",
                "../src/EbookController.h",
                "../src/EbookControls.cpp",
                "../src/EbookControls.h",
                "../src/EbookDoc.cpp",
                "../src/EbookDoc.h",
                "../src/EbookEngine.cpp",
                "../src/EbookEngine.h",
                "../src/EbookFormatter.cpp",
                "../src/EbookFormatter.h",
                "../src/EngineManager.cpp",
                "../src/EngineManager.h",
                "../src/ExternalPdfViewer.cpp",
                "../src/ExternalPdfViewer.h",
                "../src/Favorites.cpp",
                "../src/Favorites.h",
                "../src/FileHistory.cpp",
                "../src/FileHistory.h",
                "../src/FileModifications.cpp",
                "../src/FileModifications.h",
                "../src/FileThumbnails.cpp",
                "../src/FileThumbnails.h",
                "../src/HtmlFormatter.cpp",
                "../src/HtmlFormatter.h",
                "../src/ImagesEngine.cpp",
                "../src/ImagesEngine.h",
                "../src/MakeLzSA.cpp",
                "../src/Menu.cpp",
                "../src/Menu.h",
                "../src/MobiDoc.cpp",
                "../src/MobiDoc.h",
                #"../src/MuPDF_Exports.cpp",
                "../src/MuiEbookPageDef.cpp",
                "../src/MuiEbookPageDef.h",
                "../src/Notifications.cpp",
                "../src/Notifications.h",
                "../src/PagesLayoutDef.cpp",
                "../src/PagesLayoutDef.h",
                "../src/ParseCommandLine.cpp",
                "../src/ParseCommandLine.h",
                "../src/PdfCreator.cpp",
                "../src/PdfCreator.h",
                "../src/PdfEngine.cpp",
                "../src/PdfEngine.h",
                "../src/PdfSync.cpp",
                "../src/PdfSync.h",
                "../src/Print.cpp",
                "../src/Print.h",
                "../src/PsEngine.cpp",
                "../src/PsEngine.h",
                "../src/RenderCache.cpp",
                "../src/RenderCache.h",
                "../src/Search.cpp",
                "../src/Search.h",
                "../src/Selection.cpp",
                "../src/Selection.h",
                "../src/SettingsStructs.h",
                "../src/StressTesting.cpp",
                "../src/StressTesting.h",
                "../src/SumatraAbout.cpp",
                "../src/SumatraAbout.h",
                "../src/SumatraAbout2.cpp",
                "../src/SumatraAbout2.h",
                "../src/SumatraDialogs.cpp",
                "../src/SumatraDialogs.h",
                "../src/SumatraPDF.cpp",
                "../src/SumatraPDF.h",
                "../src/SumatraProperties.cpp",
                "../src/SumatraProperties.h",
                "../src/SumatraStartup.cpp",
                "../src/TableOfContents.cpp",
                "../src/TableOfContents.h",
                "../src/Tabs.cpp",
                "../src/Tabs.h",
                "../src/Tester.cpp",
                "../src/TextSearch.cpp",
                "../src/TextSearch.h",
                "../src/TextSelection.cpp",
                "../src/TextSelection.h",
                "../src/Toolbar.cpp",
                "../src/Toolbar.h",
                "../src/Trans_sumatra_txt.cpp",
                "../src/Translations.cpp",
                "../src/Translations.h",
                "../src/UnitTests.cpp",
                "../src/Version.h",
                "../src/WindowInfo.cpp",
                "../src/WindowInfo.h",
                "../src/resource.h",
                "../src/uia/Constants.h",
                "../src/uia/DocumentProvider.cpp",
                "../src/uia/DocumentProvider.h",
                "../src/uia/PageProvider.cpp",
                "../src/uia/PageProvider.h",
                "../src/uia/Provider.cpp",
                "../src/uia/Provider.h",
                "../src/uia/StartPageProvider.cpp",
                "../src/uia/StartPageProvider.h",
                "../src/uia/TextRange.cpp",
                "../src/uia/TextRange.h",
                '../src/regress/Regress.cpp',
                "../ext/synctex/synctex_parser.c",
                "../ext/synctex/synctex_parser.h",
                "../ext/synctex/synctex_parser_local.h",
                "../ext/synctex/synctex_parser_utils.c",
                "../ext/synctex/synctex_parser_utils.h",
                "../src/SumatraPDF.rc",
            ],
            'defines': [
            ],
            'link_settings': {
                'libraries': [
                    'gdiplus.lib',
                    'comctl32.lib',
                    'shlwapi.lib',
                    'Version.lib',
                    'user32.lib',
                    'kernel32.lib',
                    'gdi32.lib',
                    'ole32.lib',
                    'advapi32.lib',
                    'shell32.lib',
                    'oleaut32.lib',
                    'winspool.lib',
                    'comdlg32.lib',
                    'urlmon.lib',
                    'windowscodecs',
                    'wininet',
                    'msimg32',
                ]
            },
            'msvs_settings': {
              'VCLinkerTool': {
                'SubSystem': '2',
              },
            },
        },
    ],
}
