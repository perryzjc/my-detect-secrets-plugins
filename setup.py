from setuptools import setup, find_packages

setup(
    name='my-detect-secrets-plugins',
    version='0.1.0',
    description='Custom detect-secrets plugins',
    packages=find_packages(),
    install_requires=[
        'detect-secrets>=1.4.0',
    ],
    entry_points={
        'detect_secrets.plugins': [
            'AbsoluteFilepath = my_detect_secrets_plugins.absolute_filepath:AbsoluteFilepath',
            'AwsSensitiveInfo = my_detect_secrets_plugins.aws_sensitive_info:AwsSensitiveInfo',
            'EmailAddress = my_detect_secrets_plugins.email_address:EmailAddress',
            'IPAddress = my_detect_secrets_plugins.ip_address:IPAddress',
        ],
    },
)
