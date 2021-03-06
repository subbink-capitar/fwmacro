try:
    from setuptools import setup
    kw = {"entry_points":
          """\
[console_scripts]
fwmpp = fwmacro:fwmpp
fwmc = fwmacro:fwmc
""",
          "zip_safe": False}
except ImportError:
    from distutils.core import setup
    kw = {"scripts": ["scripts/fwmpp", "scripts/fwmc"]}

long_description = open("description.txt").read()

setup(
    name="fwmacro",
    version="0.9.4",
    description="Firewall macro compiler",
    long_description=long_description,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Topic :: System :: Networking",
        "Topic :: System :: Networking :: Firewalls",
        "Topic :: System :: Operating System",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
    keywords=[
        "Networking",
        "Systems Administration",
        "Firewall",
        "iptables",
        "ip6tables",
    ],
    author="Kees Bos",
    author_email="k.bos@capitar.com",
    url="https://github.com/keesbos/fwmacro",
    license="MIT",
    py_modules=["fwmacro"],
    packages=[],
    include_package_data=True,
    install_requires=[
        "plex",
        "netaddr",
    ],
    **kw
)
