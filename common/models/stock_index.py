from app import db



class StockIndex(db.Model):
    __tablename__ = 'stock_index'

    id = db.Column(db.Integer, primary_key=True)
    open = db.Column(db.String(255, 'utf8mb4_general_ci'), nullable=False)
    close = db.Column(db.String(255, 'utf8mb4_general_ci'), nullable=False)
    highest = db.Column(db.String(255, 'utf8mb4_general_ci'), nullable=False)
    lowest = db.Column(db.String(255, 'utf8mb4_general_ci'), nullable=False)
    code = db.Column(db.String(255, 'utf8mb4_general_ci'), nullable=False)
    time = db.Column(db.String(255, 'utf8mb4_general_ci'), nullable=False)

    def to_json(self):
        """将实例对象转化为json"""
        item = self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        return item
