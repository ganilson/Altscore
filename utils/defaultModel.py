from django.db import models
import uuid

# Este modelo, e de referencia para todos outros no SIA.


class globalModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)

    def create(cls, **kwargs):
        instance = cls(**kwargs)
        instance.save()
        return instance

    def update_fields(self, **kwargs):
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.save()

    class Meta:
        abstract = True

    # @classmethod
    # def save(cls, **kwargs):
    #     instance = cls(**kwargs)
    #     instance.save()
    #     return instance
