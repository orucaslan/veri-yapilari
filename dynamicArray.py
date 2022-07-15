import ctypes

"""
Dynamic array
"""

class DynamicArray (object):        # dynamic arrya sınıfımızı oluşturduk 
    
    #constructer 
    def __init__(self):
        self.capacity = 1               # başlangıç kapasitesi 
        self.Array = self.makeArray(self.capacity)  # array tanımlama 
        self.numberOfElements = 0       # eleman sayısı
        
    def __len__ (self):                 
        """dizinin uzunluğu"""
        return self.numberOfElements
    
    def __getitem__ (self,index):
        """verilen indeksdeki eleman"""
        
        if index >= self.numberOfElements and index < 0:       # verilen index numarasının aralığımızda olup olmadığının kontrolü
            return IndexError("indeks is out of bounds")
        
        return self.Array[index]        # aralıkda ise değeri dönüyor 
        
    def append (self , value):
        """sondan eleman ekleme"""
        
        if self.numberOfElements >= self.capacity:  # eleman eklemek için yeterli alan kontrolü
            self._resize( 2 * self.capacity )       # yeterli alan yoksa kapasiteyi iki katına çıkarıyoruz 
            
        self.Array[self.numberOfElements] = value   # elemanı sona ekledik
        self.numberOfElements += 1                  # eleman sayımızı bir arttırdık (gğncelledilk)
        
        
    def insert (self , value , index ):
        """araya eleman ekleme"""
        
        if self.numberOfElements >= self.capacity:  # eleman eklemek için yeterli alan kontrolü
            self._resize( 2 * self.capacity )       # yeterli alan yoksa kapasiteyi iki katına çıkarıyoruz 
            
        for i in range(self.numberOfElements-1, index-1 ,-1):   # araya eleman eklemek için indeksten sonraki değerleri kaydırdık
            self.Array[i+1] = self.Array[i]
            
        self.Array[index] = value   # elemanı araya ekledik
        self.numberOfElements += 1  # eleman sayısını bir arttırdık (güncelledik)
        
    def delete ( self , index ):
        """ verilen indeksdeki elemanı silme"""
        
        for i in range (index , self.numberOfElements): # aradan silinmek istenen elemanın üstüne arkasındaki değerleri kaydırdık
            self.Array[i] = self.Array[i+1]
            
        self.Array[self.numberOfElements - 1] = None    # en sonda fazladan kalan değeri sildik 
        self.numberOfElements -= 1                      # eleman sayısını bir eksilttik (güncelledik)
            
    def _resize(self , newCapacity ):
        """array kapasitesini iki katına çıkarma"""
        
        newArray = self.makeArray(newCapacity)      # yeni kapasite ile bir array oluşturuyoruz 
        
        for i in range( self.numberOfElements):     # oluşan yüksek kapasiteli arraye eski değerleri kopyalıyoruz
            newArray[i] = self.Array[i]
            
        self.Array = newArray                       # yeni arrayi eski arraye atayarak güncelliyoruz
        self.capacity = newCapacity                 # kapasite değerini güncelliyoruz
        
    def makeArray ( self , capacity ):              
        """array oluşturma"""
        return ( capacity * ctypes.py_object )      # ctypes kütüphanesini kullanarak bir array oluşturuyoruz 