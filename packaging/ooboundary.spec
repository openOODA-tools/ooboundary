Name:           ooboundary
Version:        0.1.0
Release:        1%{?dist}
Summary:        Hardware enforced kernel netfilter hook restricting agent sockets to allowed IPs.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooboundary
Source0:        ooboundary-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooboundary is a sovereign, capability-bounded EGRESS BOUNDARY written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooboundary
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooboundary-uninstall

%files
/usr/bin/ooboundary
/usr/bin/ooboundary-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
