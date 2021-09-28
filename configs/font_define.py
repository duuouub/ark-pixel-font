import time

import configs

display_name = 'Ark Pixel'
unique_name = 'ArkPixel'
output_basic_name = 'ark-pixel'
release_basic_name = 'ark-pixel-font'
version_name = '0.0.0-dev'
version_time = time.strftime("%Y%m%d")
version = f'{version_name}-{version_time}'
copyright_string = "Copyright (c) 2021, TakWolf (https://ark-pixel-font.takwolf.com), with Reserved Font Name 'Ark Pixel'."
designer = 'TakWolf'
description = 'Ark pixel font.'
vendor_url = 'https://ark-pixel-font.takwolf.com'
designer_url = 'https://takwolf.com'
license_description = 'This Font Software is licensed under the SIL Open Font License, Version 1.1.'
license_info_url = 'https://scripts.sil.org/OFL'


class FontConfig:
    def __init__(self, px, ascent_px, descent_px, em_dot_size=100):
        # 字体信息
        self.display_name = f'{display_name} {px}px'
        self.unique_name = f'{unique_name}-{px}px'
        self.style_name = 'Regular'
        # 字体参数
        self.px = px
        self.ascent_px = ascent_px
        self.descent_px = descent_px
        self.em_dot_size = em_dot_size
        self.units_per_em = px * self.em_dot_size
        self.ascent = ascent_px * self.em_dot_size
        self.descent = descent_px * self.em_dot_size
        # 文件清单
        self.output_basic_name = f'{output_basic_name}-{px}px'
        self.info_file_name = f'font-info-{px}px.md'
        self.preview_image_file_name = f'preview-{px}px.png'
        self.alphabet_txt_file_name = f'alphabet-{px}px.txt'
        self.alphabet_html_file_name = f'alphabet-{px}px.html'
        self.demo_html_file_name = f'demo-{px}px.html'
        self.release_basic_name = f'{release_basic_name}-{px}px'
        self.otf_zip_file_name = f'{self.release_basic_name}-otf-v{version}.zip'
        self.woff2_zip_file_name = f'{self.release_basic_name}-woff2-v{version}.zip'
        self.ttf_zip_file_name = f'{self.release_basic_name}-ttf-v{version}.zip'
        # 语言变种相关配置
        self.locale_flavor_configs = [FontLocaleFlavorConfig(self, locale_flavor) for locale_flavor in configs.locale_flavors]


class FontLocaleFlavorConfig:
    def __init__(self, font_config, locale_flavor):
        self.locale_flavor = locale_flavor
        # 字体信息
        self.display_name = f'{font_config.display_name} {locale_flavor.upper()}'
        self.unique_name = f'{font_config.unique_name}-{locale_flavor.upper()}'
        # 文件清单
        self.otf_file_name = f'{font_config.output_basic_name}-{locale_flavor}.otf'
        self.woff2_file_name = f'{font_config.output_basic_name}-{locale_flavor}.woff2'
        self.ttf_file_name = f'{font_config.output_basic_name}-{locale_flavor}.ttf'