def generate_required_property(attr_name):
    private_attr = f"_{attr_name}"

    @property
    def prop(self):
        value = getattr(self, private_attr, None)
        if value is None:
            raise ValueError(f"{attr_name} 속성이 설정되지 않았습니다.")
        return value

    @prop.setter
    def prop(self, value):
        setattr(self, private_attr, value)

    return prop


def generate_property(attr_name):
    private_attr = f"_{attr_name}"

    @property
    def prop(self):
        value = getattr(self, private_attr, None)
        return value

    @prop.setter
    def prop(self, value):
        setattr(self, private_attr, value)

    return prop
