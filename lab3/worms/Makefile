include $(TOPDIR)/rules.mk

PKG_NAME:=worms
PKG_RELEASE:=1

PKG_BUILD_DIR := $(BUILD_DIR)/$(PKG_NAME)
include $(INCLUDE_DIR)/package.mk

define Package/$(PKG_NAME)
  SECTION:=examples
  CATEGORY:=Examples
  TITLE:=Test apllication
  DEPENDS:=+libncurses
endef

define Package/$(PKG_NAME)/description
  Tu mogę stworzyć jakiś opis
  Ale na razie mi się nie chce.
endef

define Build/Configure
endef

define Build/Compile
        $(MAKE) -C $(PKG_BUILD_DIR) \
                CC="$(TARGET_CC)" \
                CFLAGS="$(TARGET_CFLAGS) -Wall" \
                LDFLAGS="$(TARGET_LDFLAGS)"
endef

define Package/$(PKG_NAME)/install
	$(INSTALL_DIR) $(1)/usr/bin
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/worms $(1)/usr/bin/
endef

$(eval $(call BuildPackage,$(PKG_NAME)))
