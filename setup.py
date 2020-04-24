# coding: utf-8

"""
    マネーフォワード クラウド経費API

    このページは[マネーフォワード クラウド経費](https://expense.moneyforward.com)（クラウド型の経費精算・ワークフローサービス）のAPIドキュメントです。ご利用開始の手順については、[github](https://github.com/moneyforward/expense-api-doc) をご覧ください。バグ報告や改善要望はgithub上からissue登録をして頂ければ幸いです。このドキュメントは[Swagger](http://swagger.io)の仕様で作成されています。実際にこのページでAPIの試打を行うことができます。試打を行いたい場合は、APIを利用するアプリケーションの登録の際に、Redirect URIを`https://expense.moneyforward.com/api/oauth2-redirect.html`に指定してお試しください。
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "moneyforward-ex"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="マネーフォワード クラウド経費API",
    author="OTA2000",
    author_email="yasuhiroota26@gmail.com",
    url="https://github.com/moneyforward-api-client/ex-python",
    keywords=["OpenAPI", "OpenAPI-Generator", "マネーフォワード クラウド経費API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    マネーフォワードクラウド経費のAPI
    """
)
