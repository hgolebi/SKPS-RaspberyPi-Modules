include $(TOPDIR)/rules.mk

PKG_NAME:=adc
PKG_RELEASE:=1

TARGET_CFLAGS += -std=c++11 -pthread

PKG_BUILD_DIR := $(BUILD_DIR)/$(PKG_NAME)
include $(INCLUDE_DIR)/package.mk

define Package/$(PKG_NAME)
  SECTION:=examples
  CATEGORY:=Examples
  TITLE:=Simple ad converter
  DEPENDS:=+libstdcpp
endef

define Package/$(PKG_NAME)/description
  Simple ad converter project for SKPS
endef

define Build/Configure
endef

define Build/Compile
        $(MAKE) -C $(PKG_BUILD_DIR) \
        LIBS="-nodefaultlibs -lgcc -lc -lstdc++" \
        CXX="$(TARGET_CXX)" \
        CXXFLAGS="$(TARGET_CXXFLAGS) $(EXTRA_CPPFLAGS) -nostdinc++" \
        LDFLAGS="$(TARGET_LDFLAGS)"
endef

define Package/$(PKG_NAME)/install
	$(INSTALL_DIR) $(1)/usr/bin
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/adc $(1)/usr/bin/
endef

$(eval $(call BuildPackage,$(PKG_NAME)))
